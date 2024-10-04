import uuid

class SessionLayer:
    def establish_session(self, data):
        session_id = str(uuid.uuid4())
        print(f"Session Layer: Establishing session with ID: {session_id}")
        session_data = f"SessionID({session_id}):{data}"
        return session_data

    def end_session(self, data):
        print("Session Layer: Ending session and removing session ID")
        return data.split(":", 1)[1]
