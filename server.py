from osi_layers.physical import PhysicalLayer
from osi_layers.data_link import DataLinkLayer
from osi_layers.network import NetworkLayer
from osi_layers.transport import TransportLayer
from osi_layers.session import SessionLayer
from osi_layers.presentation import PresentationLayer
from osi_layers.application import ApplicationLayer

def main():
    # Physical (received via socket)
    physical_layer = PhysicalLayer()
    received_data = physical_layer.receive_data()

    # Data Link (Check CRC)
    data_link_layer = DataLinkLayer()
    routed_data = data_link_layer.unframe_data(received_data)

    # Network
    network_layer = NetworkLayer()
    segmented_data = network_layer.unroute_data(routed_data)

    # Transport
    transport_layer = TransportLayer(protocol="TCP")
    session_data = transport_layer.reassemble_data(segmented_data)

    # Session 
    session_layer = SessionLayer()
    encoded_data = session_layer.end_session(session_data)

    # Presentation (Decrypted base64)
    presentation_layer = PresentationLayer()
    processed_data = presentation_layer.decode_data(encoded_data)

    # Application
    app_layer = ApplicationLayer()
    app_layer.show_data(processed_data)

if __name__ == "__main__":
    main()
