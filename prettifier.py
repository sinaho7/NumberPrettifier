class NumberPrettifier:
    """
    A class to convert numbers into prettified strings with K (thousands), M (millions), B (billions), or T (trillions).
    """

    units = (
        (1_000_000_000_000, 'T'),
        (1_000_000_000, 'B'),
        (1_000_000, 'M'),
        (1_000, 'K'),
    )

    @staticmethod
    def prettify(num):
        """
        Converts a number into a prettified string with K (thousands), M (millions), B (billions), or T (trillions).
        
        Parameters:
        num (int or float): The number to prettify.
        
        Returns:
        str: The prettified string representation of the number.
        """
        
        # Handle the case where the number is less than 1000
        if abs(num) < 1_000:
            return str(num)
        
        # Determine the appropriate unit and truncate the number
        for divisor, unit in NumberPrettifier.units:
            if abs(num) >= divisor:
                truncated_num = round(num / divisor, 1)
                # Format number to remove .0 for whole numbers
                if truncated_num.is_integer():
                    truncated_num = int(truncated_num)
                return f"{truncated_num}{unit}"
        
        # In case the number doesn't fall into any of the categories 
        return str(num)
