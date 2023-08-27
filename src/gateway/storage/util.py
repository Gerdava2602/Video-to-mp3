import pika, json


def upload(file, fs, channel, access):
    try:
        # Add the file to the database
        fid = fs.put(file)
    except Exception as err:
        return "internal error", 500

    # Create a message to send to the queue
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    # Send the message to the queue
    try:
        channel.basic_publish(
            exchange="",  # Default exchange
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # Our messages our persist in the queue even if the server goes down
            ),
        )
    except:
        fs.delete(fid)
        return "internal error", 500
