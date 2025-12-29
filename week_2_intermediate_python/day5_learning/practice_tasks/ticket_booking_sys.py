class SeatAlreadyBookedError(Exception):
    def __init__(self, seat_no):
        super().__init__(f"Seat {seat_no} is already booked!")

class TicketBookingSystem:
    def __init__(self, total_seat):
        self.seats = {i: 'available' for i in range(1,total_seat+1)}
    try:
        def book_seat(self, seat_no):
            if seat_no not in self.seats:
                raise ValueError("Invalid seat number")
            if self.seat[seat_no] == 'booked':
                raise SeatAlreadyBookedError(seat_no)
            self.seats[seat_no] = 'booked'
            print(f"Seat {seat_no} booked successfully")
    except SeatAlreadyBookedError as s:
        print(s)
    except ValueError as v:
        print(v)

    def show_remaining_seats(self):
        remaining = sum(1 for s in self.seats.values() if s == "available")
        print(f"Remaining seats: {remaining}")

    def show_all_seats(self):
        for seat, status in self.seats.items():
            print(f"{seat} → {status}")

tbs = TicketBookingSystem(52)
tbs.show_all_seats()