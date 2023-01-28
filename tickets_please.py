def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    ticket_number = 100
    i = 0
    ticket_source = source[0:3]
    ticket_destination = destination[0:3]
    space = ":"
    while i < no_of_passengers:
        ticket_number += 1
        ticket = airline + space + str(ticket_source) + space + str(ticket_destination) + space + str(ticket_number)
        ticket_number_list.append(ticket)
        i += 1
    if no_of_passengers < 5:
        return ticket_number_list
    else:
        return ticket_number_list[-5:]


# Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 7))
