import pyarrow.flight as flight
import pyarrow as pa


if __name__ == "__main__":

    location="grpc://arrowflight-server:8815"
    client = flight.connect(location, disable_server_verification=True)
    ticket_name="table_int"
    response = client.do_get(flight.Ticket(ticket_name)).read_all()
    print(response)
