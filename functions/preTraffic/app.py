def lambda_handler(event, context):
    # Aquí puedes agregar cualquier validación o lógica antes del tráfico
    print("Pre-traffic validation passed!")
    return {
        'statusCode': 200,
        'body': "Pre-traffic hook passed!"
    }
