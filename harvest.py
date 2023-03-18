############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self,
        name,
        code,
        first_harvest,
        color,
        is_seedless,
        is_bestseller,
    ):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

    # def repr(self):
    #     return f"<melon name = {self.name}>"
    """Question for Meggin: 
    When will we have to call this definition in order to use it with other methods/functions?"""


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    #cat = Cat()
    muskmelon = MelonType("muskmelon", "musk", 1998, "green", True, True)
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)
    casaba = MelonType("Casaba", "cas", 2003, "orange", True, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)
    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", True, False)
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)
    yellow_watermelon = MelonType("Yellow Watermelon", "yw", 2013, "yellow",
                                  True, True)
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    # print(all_melon_types)
    return all_melon_types


melon_types = make_melon_types()
# print(melon_types)
# # loop through and print the pairing of each one
for items in melon_types:

    print(f"{items.pairings} {items.name}")


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for items in melon_types:
        pairing_string = ",".join(items.pairings)
        print(f"{items.name} pairs with ")
        print(f"- {pairing_string}")


print_pairing_info(melon_types)
# Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for item in melon_types:
        # print(item)
        melon_dict[item.code] = item

    return melon_dict


print(make_melon_type_lookup(melon_types))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
