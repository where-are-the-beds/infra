## This project allows user to track availability of beds in the US

How to run
```
1. Build and activate a virtual environment: 
python3 -m venv env
source env/bin/activate
2. Install packages:
pip3 install aws_cdk.core
pip3 install aws_cdk.aws_ec2
pip3 install aws_cdk.aws_ecs
3. Install AWS CDK CLI:
npm install aws-cdk
4. Boostrap infrastructure:
node_modules/aws-cdk/bin/cdk bootstrap
5. Deploy infrastructure:
node_modules/aws-cdk/bin/cdk deploy
```