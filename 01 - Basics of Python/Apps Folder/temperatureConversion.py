print("Welcome to temperature conversion...")
print("You can use type of conversion: KC, CK, CF, CR, KF, KR, FC, FK, FR, RC, RK, RF")
print("For instance, KC: It express conversion from Kelvin to Celsius.")
print("---------------------------------------------------------------")

input_1 = input("Conversion: ")

class temperature_convesion:

    def __init__(self, conversion):

        self.conversion = conversion

    def conversion_ck(self):

        if self.conversion == "KC" or self.conversion == "kc":

            input_2 = int(input("Kelvin: "))
            C = input_2 - 273
            print("{} Kelvin is {} Celsius.".format(input_2, C))

        elif self.conversion == "CK" or self.conversion == "ck":

            input_3 = int(input("Celsius: "))
            K = input_3 - 273
            print("{} Celsius is {} Kelvin.".format(input_3, K))

        elif self.conversion == "CF" or self.conversion == "cf":

            input_4 = int(input("Celsius: "))
            F = (9 * input_4 + 160)/5
            print("{} Celsius is {} Fahrenheit.".format(input_4, F))

        elif self.conversion == "CR" or self.conversion == "cr":

            input_5 = int(input("Celsius: "))
            R = (4 * input_5) / 5
            print("{} Celsius is {} Reumur.".format(input_5, R))

        elif self.conversion == "KF" or self.conversion == "kf":

            input_6 = int(input("Kelvin: "))
            F = 9 * (input_6 - 273) / 5 + 32
            print("{} Kelvin is {} Fahrenheit.".format(input_6, F))

        elif self.conversion == "KR" or self.conversion == "kr":

            input_7 = int(input("Kelvin: "))
            R = 4 * (input_7 - 273) / 5
            print("{} Kelvin is {} Reumur.".format(input_7, R))

        elif self.conversion == "FC" or self.conversion == "fc":

            input_8 = int(input("Fahrenheit: "))
            C = 5 * (input_8 - 32) / 9
            print("{} Fahrenheit is {} Celsius.".format(input_8, C))

        elif self.conversion == "FK" or self.conversion == "fk":

            input_9 = int(input("Fahrenheit: "))
            K = 5 * (input_9 - 32) / 9 + 273
            print("{} Fahrenheit is {} Kelvin.".format(input_9, K))

        elif self.conversion == "FR" or self.conversion == "fr":

            input_10 = int(input("Fahrenheit: "))
            R = 4 * (input_10 - 32) / 9
            print("{} Fahrenheit is {} Reumur.".format(input_10, R))

        elif self.conversion == "RC" or self.conversion == "rc":

            input_11 = int(input("Reumur: "))
            C = (5 * input_11) / 4
            print("{} Reumur is {} Celsius.".format(input_11, C))

        elif self.conversion == "RF" or self.conversion == "rf":

            input_12 = int(input("Reumur: "))
            F = (9 * input_12) / 4 + 32
            print("{} Reumur is {} Fahrenheit.".format(input_12, F))

        elif self.conversion == "RK" or self.conversion == "rk":

            input_13 = int(input("Reumur: "))
            K = (5 * input_13) / 4 + 273
            print("{} Reumur is {} Kelvin.".format(input_13, K))

        else:
            pass

result = temperature_convesion(conversion=input_1)
result.conversion_ck()