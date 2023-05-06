import json
from plugin_loader import load_plugin

def lambda_handler(event, context):
    message = event['message']
    plugin_name = event['plugin']
    plugin = load_plugin(plugin_name)
    processed_message = plugin.process(message)

    response = { 
        'original_message': message,
        'message': processed_message,
        'plugin_used': plugin_name  
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }