"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        "Initialize melon order attributes."

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species.lower() == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax and fees"""

        if self.qty < 10:
            flat_fee = 3
            return super(InternationalMelonOrder, self).get_total() + flat_fee

        return super(InternationalMelonOrder, self).get_total()


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order by the US Government."""

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """Marks melon as True after inspection."""

        self.passed_inspection = passed
