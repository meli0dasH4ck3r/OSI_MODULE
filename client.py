from osi_layers.application import ApplicationLayer
from osi_layers.presentation import PresentationLayer
from osi_layers.session import SessionLayer
from osi_layers.transport import TransportLayer
from osi_layers.network import NetworkLayer
from osi_layers.data_link import DataLinkLayer
from osi_layers.physical import PhysicalLayer

def main():
    # Data 
    data = "Hello from client to server !"
    
    # Application
    app_layer = ApplicationLayer()
    processed_data = app_layer.process_data(data)

    # Presentation (Encrypted base64)
    presentation_layer = PresentationLayer()
    encoded_data = presentation_layer.encode_data(processed_data)

    # Session
    session_layer = SessionLayer()
    session_data = session_layer.establish_session(encoded_data)

    # Transport
    transport_layer = TransportLayer(protocol="TCP")
    segmented_data = transport_layer.segment_data(session_data)

    # Network
    network_layer = NetworkLayer()
    routed_data = network_layer.route_data(segmented_data)

    # Data Link 
    data_link_layer = DataLinkLayer()
    framed_data = data_link_layer.frame_data(routed_data)

    # Physical (via socket)
    physical_layer = PhysicalLayer()
    physical_layer.transmit_data(framed_data)

if __name__ == "__main__":
    main()
