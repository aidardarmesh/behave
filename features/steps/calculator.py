from behave import *
from cucumber import Basket


@given('basket has "{initial}" cucumbers')
def step_impl(context, initial):
    context.basket = Basket(int(initial))


@when('basket changed weight on "{change}" cucumbers')
def stem_impl(context, change):
    context.basket.weight += int(change)


@then('basket contains "{output}" cucumbers')
def step_impl(context, output):
    context.basket.weight == int(output)

