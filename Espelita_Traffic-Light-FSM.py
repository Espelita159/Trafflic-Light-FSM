class TrafficLightFSM:
    def __init__(self):
        self.state = 0

    def on_event(self, event):
        if event == 'Timer Expires' and self.state != 3:
            if self.state == 0:
                self.state = 1
            elif self.state == 1:
                self.state = 2
            elif self.state == 2:
                self.state = 0
        
        # Final State
        elif event in ['Emergency Mode', 'Maintenance Mode']:
            self.state = 3

        elif event == 'Reset' and self.state == 3:
            self.state = 0

    def __str__(self):
        state_names = {0: 'Red', 1: 'Green', 2: 'Yellow', 3: 'Emergency/Maintenance Mode'}
        return f'Traffic light is currently {state_names[self.state]}.'
    

def simulate_traffic_light():
    fsm = TrafficLightFSM()

    while True:
        print(f"\n{fsm}")
        print("Choose an event:")
        print("1. Timer Expires")
        print("2. Emergency Mode")
        print("3. Maintenance Mode")
        print("4. Reset")
        print("5. Exit")

        user_input = input("Enter the number of the events you want: ")

        if user_input == '1':
            fsm.on_event('Timer Expires')
        elif user_input == '2':
            fsm.on_event('Emergency Mode')
        elif user_input == '3':
            fsm.on_event('Maintenance Mode')
        elif user_input == '4':
            fsm.on_event('Reset')
        elif user_input == '5':
            print("Exiting...")
            break
        else:
            print("Invalid Input")


simulate_traffic_light()