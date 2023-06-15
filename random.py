import os
import time

this_lambda_arn = 'arn:aws:lambda:eu-north-1:960346235350:function:send_notification'
this_layer_arn = 'arn:aws:lambda:eu-north-1:960346235350:layer:send_notification_layer'
file_path = "lambda_function.py"
compressed_file_path = "python.zip"

os.system('mkdir python')
os.system('cp ./requirements.txt ./python/requirements.txt')
os.system('touch ./python/__init__.py')
os.system('pip3 install -r ./python/requirements.txt -t ./python')
os.system('zip -r layer.zip python')
os.system(f'aws lambda publish-layer-version --layer-name {this_layer_arn} --description "send notification '
          f'dependencies" --license-info "MIT" --zip-file fileb://layer.zip --compatible-runtimes python3.10')
lambda_conf = os.popen(f'aws lambda list-layer-versions --layer-name {this_layer_arn} --query "LayerVersions['
                       f'0].LayerVersionArn" --output text').read()
last_layer_version = lambda_conf.split("\n")[0]
os.system(f"zip -r -u '{compressed_file_path}' '{file_path}'")
os.system(f'aws lambda update-function-configuration --function-name {this_lambda_arn} --layers {last_layer_version}')
# give 20 seconds to let lambda function update his configuration
time.sleep(20)
update_command = f"aws lambda update-function-code --function-name {this_lambda_arn} --zip-file fileb://{compressed_file_path} --publish"
os.system(update_command)
