import logging
import sys
import boto3
import os

SERVICE_ID='ts00934'

subnet_id = os.environ['SUBNET_ID']

client = boto3.client('ec2')

def setup_logging():
    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)
    h = logging.StreamHandler(sys.stdout)
    formatter = '%(asctime)s log_level=%(levelname)s service_name="subnet-ip-evaluator-lambda", %(message)s'
    h.setFormatter(logging.Formatter(formatter))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)
    return logger


logger = setup_logging()


def desc_subnet():
    response = client.describe_subnets(
        Filters=[
            {
                'Name': 'subnet-id',
                'Values': [
                    subnet_id,
                ],
            },
        ],

    )
    return response['Subnets'][0]['AvailableIpAddressCount']

def desc_network_interface():
     return client.describe_network_interfaces(
            Filters=[
                {
                    'Name': 'subnet-id',
                    'Values': [
                        subnet_id,
                    ],
                },
                {
                    'Name': 'status',
                    'Values': [
                        'available',
                    ],
                }
            ]
        )

def get_network_interface_ids(network_interface):
    network_interface_ids = []
    for network_interface_id in network_interface['NetworkInterfaces']:
        network_interface_ids.append(network_interface_id['NetworkInterfaceId'])
    return network_interface_ids

def del_network_interface_ids(network_interface_ids):
    for interface_id in network_interface_ids:
        try:
            response = client.delete_network_interface(
                NetworkInterfaceId=interface_id
            )
        except Exception as error:
             logger.error('request_id="' + LAMBDA_REQUEST_ID + '", service_id={}, '
                                                                      ' event_severity="{}", exception_message="{}",'
                                                                      'message="Error in del_network_interface_id",'
                                 .format(SERVICE_ID, 'critical',str(error)))

def lambda_handler(event, context):
    try:
        global LAMBDA_REQUEST_ID
        if event.get('request_id') is None:
            logger.info('='*30+'request_id not present'+'='*30+'{}'.format(context.aws_request_id))
            LAMBDA_REQUEST_ID = context.aws_request_id
        else:
            logger.info('='*30+'request_id present'+'='*30+'{}'.format(event['request_id']))
            LAMBDA_REQUEST_ID = event['request_id']
        logger.info(f'''request_id={LAMBDA_REQUEST_ID}, event={str(event)}''')
        #print(subnet_id)
        table = event['table']
        index =    event['index']
        step = event['step']
        count = event['count']
        index += step

        network_interface = desc_network_interface()
        network_interface_ids = get_network_interface_ids(network_interface)
        del_network_interface_ids(network_interface_ids)

        available_ip_addr_count = desc_subnet()
        is_ip_available = True
        if available_ip_addr_count < 15 :
            is_ip_available = False

        logger.info('IP avaialable : '+ str(is_ip_available) +' for table: '+table+' in subnet_id : '+subnet_id+' AvailableIpAddressCount : '+str(available_ip_addr_count))

        return {
            'is_ip_available': is_ip_available,
            'continue' : index <= count,
            'index': index,
            'step' : step,
            'count' :count,
            'table': table
        }
    except Exception as error:
        logger.error('request_id="' + LAMBDA_REQUEST_ID + '", service_id={}, '
                                                          ' event_severity="{}",table="{}", exception_message="{}",'
                                                          'message="Error in lambda",'
                     .format(SERVICE_ID, 'critical',table, str(error)))
