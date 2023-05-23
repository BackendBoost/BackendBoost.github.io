# sudo apt upgrade

# curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# sudo apt-get install unzip
# unzip awscliv2.zip
# sudo ./aws/install
# sudo apt get install python3-pip
# pip install boto3
# sudo vi ec2CommandSend.py

# https://stackoverflow.com/questions/47034797/invalidinstanceid-an-error-occurred-invalidinstanceid-when-calling-the-sendco

# https://aws.amazon.com/getting-started/hands-on/remotely-run-commands-ec2-instance-systems-manager/


import boto3
def execute_commands_on_linux_instances(client, commands, instance_ids):
    """Runs commands on remote linux instances
    :param client: a boto/boto3 ssm client
    :param commands: a list of strings, each one a command to execute on the instances
    :param instance_ids: a list of instance_id strings, of the instances on which to execute the command
    :return: the response from the send_command function (check the boto3 docs for ssm client.send_command() )
    """

    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp

# Example use:
ssm_client = boto3.client('ssm') # Need your credentials here
commands = ['echo "hello world"']
instance_ids = ['i-0663d645a5dfc27b9']
x = execute_commands_on_linux_instances(ssm_client, commands, instance_ids)
print(x)
