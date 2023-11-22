import math

class PhysicsCalculator:
    def __init__(self):
        pass

    def get_user_choice(self):
        print("\nPhysics Calculator Menu:")
        print("1. Kinematic Equations")
        print("2. Gravitational Force")
        print("3. Energy Calculations")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        return choice

    def kinematic_equations(self):
        print("\nKinematic Equations:")
        # Input values
        initial_velocity = float(input("Enter initial velocity (m/s): "))
        final_velocity = float(input("Enter final velocity (m/s): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        time = float(input("Enter time (s): "))

        # Kinematic equations
        displacement = (initial_velocity + final_velocity) * time / 2
        final_velocity_squared = initial_velocity**2 + 2 * acceleration * displacement

        # Output results
        print(f"Displacement: {displacement} meters")
        print(f"Final Velocity (squared): {final_velocity_squared} m^2/s^2")

    def gravitational_force(self):
        print("\nGravitational Force:")
        # Input values
        mass1 = float(input("Enter mass of object 1 (kg): "))
        mass2 = float(input("Enter mass of object 2 (kg): "))
        distance = float(input("Enter distance between the objects (m): "))

        # Gravitational force formula
        gravitational_force = (6.674 * 10**-11) * (mass1 * mass2) / distance**2

        # Output result
        print(f"Gravitational Force: {gravitational_force} Newtons")

    def energy_calculations(self):
        print("\nEnergy Calculations:")
        # Input values
        mass = float(input("Enter mass (kg): "))
        height = float(input("Enter height (m): "))
        gravitational_acceleration = 9.8  # Acceleration due to gravity

        # Potential energy formula
        potential_energy = mass * gravitational_acceleration * height

        # Output result
        print(f"Potential Energy: {potential_energy} Joules")

    def run_calculator(self):
        while True:
            choice = self.get_user_choice()

            if choice == '1':
                self.kinematic_equations()
            elif choice == '2':
                self.gravitational_force()
            elif choice == '3':
                self.energy_calculations()
            elif choice == '4':
                print("Exiting the Physics Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    physics_calculator = PhysicsCalculator()
    physics_calculator.run_calculator()
