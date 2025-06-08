import re

class StringCalculator:
    def Add(self, numbers: str) -> int:
        """
        Adds numbers provided in a string, supporting commas, newlines, custom delimiters,
        and multiple delimiters. Throws an exception for negative numbers and ignores numbers > 1000.
        
        Args:
            numbers: A string containing numbers (e.g., "", "1", "1,2", "//;\n1;2", "1\n2,3").
        
        Returns:
            The sum of the numbers as an integer.
        
        Raises:
            ValueError: If negative numbers are present, with all negatives listed in the message.
        """
        # Handle empty string
        if not numbers:
            return 0
        
        # Default delimiters: comma and newline
        delimiters = [",", "\n"]
        numbers_to_parse = numbers
        
        # Check for custom delimiter(s)
        if numbers.startswith("//"):
            # Extract delimiter section and numbers
            parts = numbers.split("\n", 1)
            if len(parts) < 2:
                raise ValueError("Invalid custom delimiter format")
            
            delimiter_line, numbers_to_parse = parts
            # Remove "//" prefix
            delimiter_line = delimiter_line[2:]
            
            # Handle multiple delimiters (e.g., [*][%]) or single delimiter (e.g., ; or ***)
            if delimiter_line.startswith("["):
                # Extract delimiters between square brackets
                delimiters = []
                pattern = r"\[(.*?)\]"
                matches = re.findall(pattern, delimiter_line)
                if not matches:
                    raise ValueError("Invalid delimiter specification")
                delimiters.extend(matches)
            else:
                # Single delimiter (e.g., ;)
                delimiters = [delimiter_line]
        
        # Parse numbers
        number_list = []
        # Escape special regex characters in delimiters
        escaped_delimiters = [re.escape(d) for d in delimiters]
        # Create regex pattern to split on any delimiter
        split_pattern = "|".join(escaped_delimiters)
        number_strings = re.split(split_pattern, numbers_to_parse)
        
        # Convert strings to integers, validate, and collect numbers
        negatives = []
        for num_str in number_strings:
            num_str = num_str.strip()
            if not num_str:
                continue  # Skip empty entries
            try:
                num = int(num_str)
                if num < 0:
                    negatives.append(num)
                elif num <= 1000:  # Ignore numbers > 1000
                    number_list.append(num)
            except ValueError:
                raise ValueError(f"Invalid number format: {num_str}")
        
        # Check for negative numbers
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        # Return sum
        return sum(number_list)