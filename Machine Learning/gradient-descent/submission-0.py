class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        minimizer = init 
        # Derivative:         f'(x) = 2x
        for _ in range(iterations):
            derivative = 2 * minimizer
            minimizer = minimizer - learning_rate * derivative

        # Update rule:        x = x - learning_rate * f'(x)
        return round(minimizer, 5)
        # Round final answer to 5 decimal places
        pass
