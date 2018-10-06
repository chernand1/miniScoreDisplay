import RPi.GPIO as GPIO

class multi_axis_switch:

    # right_contact = 5, left_contact = 6, up_contact = 12, down_contact = 22, push_contact = 23
    def __init__(self, right_contact = 22, left_contact = 12, up_contact = 23, down_contact = 5, push_contact = 6):
        self.right_contact = right_contact
        self.left_contact = left_contact
        self.up_contact = up_contact
        self.down_contact = down_contact
        self.push_contact = push_contact

        self.push_contact_state = 1

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.right_contact, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.left_contact, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.up_contact, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.down_contact, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.push_contact, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def init_event(self):

        GPIO.add_event_detect(self.push_contact, GPIO.FALLING)
        GPIO.add_event_detect(self.down_contact, GPIO.FALLING)

        def switch_push(cast):
            print("Push")
        GPIO.add_event_callback(self.push_contact, switch_push)

        def switch_down(cast):
            print("Down")
        GPIO.add_event_callback(self.down_contact, switch_down)


    def switch_state(self):
        return GPIO.input(self.right_contact), GPIO.input(self.left_contact), GPIO.input(self.up_contact), GPIO.input(self.down_contact), GPIO.input(self.push_contact)

    def switch_state_name(self):
        if GPIO.input(self.right_contact) == 0:
            return "Right Switch"
        if GPIO.input(self.left_contact) == 0:
            return "Left Switch"
        if GPIO.input(self.up_contact) == 0:
            return "Up Switch"
        if GPIO.input(self.down_contact) == 0:
            return "Down Switch"
        if GPIO.input(self.push_contact) == 0:
            return "Push Switch"

    def return_sw_right(self):
        return GPIO.input(self.right_contact)

    def return_sw_left(self):
        return GPIO.input(self.left_contact)

    def return_sw_up(self):
        return GPIO.input(self.up_contact)

    def return_sw_down(self):
        return GPIO.input(self.down_contact)

    def return_sw_push(self):
        return GPIO.input(self.push_contact)
