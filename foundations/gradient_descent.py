class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x_final = init

        while iterations:
            x_final -= learning_rate *(2*x_final)
            iterations -= 1
        
        return round(x_final, 5)
