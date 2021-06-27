from itertools import count, tee


class Bouncy:
    def __init__(self, porcentage):
        """
        print the number bouncy
        :type porcentage: int -> this is porcentage of the bouncy
        """
        nums = count(1)
        rebound = self.sum_number(map(lambda number: float(self.is_rebound(number)), count(1)))
        bouncy = next(
            (
                number
                for number, number_b in zip(nums, rebound)
                if number_b / number == (porcentage / 100)
            )
        )
        print(bouncy)

    def pairs(self, iterable):
        """
        return a list convert map, produces new list
        :type number: int
        """
        # tee() get iterator independent (default 2) with a input
        a, b = tee(iterable)
        # next() return next element in the secuence
        next(b, None)
        # zip() return new iterator
        return zip(a, b)

    def digits(self, number):
        """
        return a list convert map, produces new list
        :type number: int
        """
        return list(map(int, str(number)))

    def increase(self, number):
        """
        return the elements as long as the previous number is less than or equal to the current one
        :type number: int
        """
        return all(prev <= curr for prev, curr in self.pairs(self.digits(number)))

    def decrease(self, number):
        """
        return the elements as long as the previous number is greater than or equal to the current one
        :type number: int
        """
        return all(prev >= curr for prev, curr in self.pairs(self.digits(number)))

    def is_rebound(self, number):
        """
        return the elements is rebound
        :type number: int
        """
        return not self.increase(number) and not self.decrease(number)

    def sum_number(self, iterable):
        """
        return a element sum total
        :type iterable: list
        """
        total = 0
        for element in iterable:
            total += element
            yield total


test = Bouncy(99)
