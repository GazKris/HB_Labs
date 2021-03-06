"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code='US'):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == 'Christmas':
            base_price *= 1.5
        total = ((1 + self.tax) * self.qty * base_price)
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_total(self):
        """Calculate price, including tax and fees."""

        total = super().get_total()
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """An US-government melon order."""

    tax = 0
    passed_inspection = False
    order_type = "government"

    def mark_inspection(self, passed):
        """Records the melon has passed inspection."""

        self.passed_inspection = passed
