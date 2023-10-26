# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.subscription_schedule import SubscriptionSchedule
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class Quote(
    CreateableAPIResource["Quote"],
    ListableAPIResource["Quote"],
    UpdateableAPIResource["Quote"],
):
    """
    A Quote is a way to model prices that you'd like to provide to a customer.
    Once accepted, it will automatically create an invoice, subscription or subscription schedule.
    """

    OBJECT_NAME: ClassVar[Literal["quote"]] = "quote"
    if TYPE_CHECKING:

        class AcceptParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CreateParams(RequestOptions):
            application_fee_amount: NotRequired["Literal['']|int|None"]
            """
            The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
            """
            application_fee_percent: NotRequired["Literal['']|float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
            """
            automatic_tax: NotRequired["Quote.CreateParamsAutomaticTax|None"]
            """
            Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
            """
            customer: NotRequired["str|None"]
            """
            The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
            """
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates that will apply to any line item that does not have `tax_rates` set.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
            """
            discounts: NotRequired[
                "Literal['']|List[Quote.CreateParamsDiscount]|None"
            ]
            """
            The discounts applied to the quote. You can only set up to one discount.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            expires_at: NotRequired["int|None"]
            """
            A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
            """
            footer: NotRequired["Literal['']|str|None"]
            """
            A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
            """
            from_quote: NotRequired["Quote.CreateParamsFromQuote|None"]
            """
            Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
            """
            header: NotRequired["Literal['']|str|None"]
            """
            A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
            """
            invoice_settings: NotRequired[
                "Quote.CreateParamsInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            line_items: NotRequired["List[Quote.CreateParamsLineItem]|None"]
            """
            A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            on_behalf_of: NotRequired["Literal['']|str|None"]
            """
            The account on behalf of which to charge.
            """
            subscription_data: NotRequired[
                "Quote.CreateParamsSubscriptionData|None"
            ]
            """
            When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
            """
            test_clock: NotRequired["str|None"]
            """
            ID of the test clock to attach to the quote.
            """
            transfer_data: NotRequired[
                "Literal['']|Quote.CreateParamsTransferData|None"
            ]
            """
            The data with which to automatically create a Transfer for each of the invoices.
            """

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            """
            The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
            """
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class CreateParamsSubscriptionData(TypedDict):
            description: NotRequired["str|None"]
            """
            The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription.
            """
            effective_date: NotRequired[
                "Literal['']|Literal['current_period_end']|int|None"
            ]
            """
            When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. When updating a subscription, the date of which the subscription will be updated using a subscription schedule. The special value `current_period_end` can be provided to update a subscription at the end of its current period. The `effective_date` is ignored if it is in the past when the quote is accepted.
            """
            trial_period_days: NotRequired["Literal['']|int|None"]
            """
            Integer representing the number of trial period days before the customer is charged for the first time.
            """

        class CreateParamsLineItem(TypedDict):
            price: NotRequired["str|None"]
            """
            The ID of the price object. One of `price` or `price_data` is required.
            """
            price_data: NotRequired["Quote.CreateParamsLineItemPriceData|None"]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
            """
            quantity: NotRequired["int|None"]
            """
            The quantity of the line item.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
            """

        class CreateParamsLineItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            recurring: NotRequired[
                "Quote.CreateParamsLineItemPriceDataRecurring|None"
            ]
            """
            The recurring components of a price such as `interval` and `interval_count`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class CreateParamsLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class CreateParamsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            """
            Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
            """

        class CreateParamsFromQuote(TypedDict):
            is_revision: NotRequired["bool|None"]
            """
            Whether this quote is a revision of the previous quote.
            """
            quote: str
            """
            The `id` of the quote that will be cloned.
            """

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool
            """
            Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
            """

        class FinalizeQuoteParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            expires_at: NotRequired["int|None"]
            """
            A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
            """

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            """
            The ID of the customer whose quotes will be retrieved.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired[
                "Literal['accepted', 'canceled', 'draft', 'open']|None"
            ]
            """
            The status of the quote.
            """
            test_clock: NotRequired["str|None"]
            """
            Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.
            """

        class ListComputedUpfrontLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ModifyParams(RequestOptions):
            application_fee_amount: NotRequired["Literal['']|int|None"]
            """
            The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
            """
            application_fee_percent: NotRequired["Literal['']|float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
            """
            automatic_tax: NotRequired["Quote.ModifyParamsAutomaticTax|None"]
            """
            Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
            """
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            """
            Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
            """
            customer: NotRequired["str|None"]
            """
            The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
            """
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates that will apply to any line item that does not have `tax_rates` set.
            """
            description: NotRequired["Literal['']|str|None"]
            """
            A description that will be displayed on the quote PDF.
            """
            discounts: NotRequired[
                "Literal['']|List[Quote.ModifyParamsDiscount]|None"
            ]
            """
            The discounts applied to the quote. You can only set up to one discount.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            expires_at: NotRequired["int|None"]
            """
            A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
            """
            footer: NotRequired["Literal['']|str|None"]
            """
            A footer that will be displayed on the quote PDF.
            """
            header: NotRequired["Literal['']|str|None"]
            """
            A header that will be displayed on the quote PDF.
            """
            invoice_settings: NotRequired[
                "Quote.ModifyParamsInvoiceSettings|None"
            ]
            """
            All invoices will be billed using the specified settings.
            """
            line_items: NotRequired["List[Quote.ModifyParamsLineItem]|None"]
            """
            A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            on_behalf_of: NotRequired["Literal['']|str|None"]
            """
            The account on behalf of which to charge.
            """
            subscription_data: NotRequired[
                "Quote.ModifyParamsSubscriptionData|None"
            ]
            """
            When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
            """
            transfer_data: NotRequired[
                "Literal['']|Quote.ModifyParamsTransferData|None"
            ]
            """
            The data with which to automatically create a Transfer for each of the invoices.
            """

        class ModifyParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            """
            The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
            """
            amount_percent: NotRequired["float|None"]
            """
            A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class ModifyParamsSubscriptionData(TypedDict):
            description: NotRequired["Literal['']|str|None"]
            """
            The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription.
            """
            effective_date: NotRequired[
                "Literal['']|Literal['current_period_end']|int|None"
            ]
            """
            When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. When updating a subscription, the date of which the subscription will be updated using a subscription schedule. The special value `current_period_end` can be provided to update a subscription at the end of its current period. The `effective_date` is ignored if it is in the past when the quote is accepted.
            """
            trial_period_days: NotRequired["Literal['']|int|None"]
            """
            Integer representing the number of trial period days before the customer is charged for the first time.
            """

        class ModifyParamsLineItem(TypedDict):
            id: NotRequired["str|None"]
            """
            The ID of an existing line item on the quote.
            """
            price: NotRequired["str|None"]
            """
            The ID of the price object. One of `price` or `price_data` is required.
            """
            price_data: NotRequired["Quote.ModifyParamsLineItemPriceData|None"]
            """
            Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
            """
            quantity: NotRequired["int|None"]
            """
            The quantity of the line item.
            """
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            """
            The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
            """

        class ModifyParamsLineItemPriceData(TypedDict):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            product: str
            """
            The ID of the product that this price will belong to.
            """
            recurring: NotRequired[
                "Quote.ModifyParamsLineItemPriceDataRecurring|None"
            ]
            """
            The recurring components of a price such as `interval` and `interval_count`.
            """
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            """
            Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            """
            unit_amount: NotRequired["int|None"]
            """
            A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
            """
            unit_amount_decimal: NotRequired["str|None"]
            """
            Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            """

        class ModifyParamsLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            """
            Specifies billing frequency. Either `day`, `week`, `month` or `year`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
            """

        class ModifyParamsInvoiceSettings(TypedDict):
            days_until_due: NotRequired["int|None"]
            """
            Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
            """

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            """
            ID of the coupon to create a new discount for.
            """
            discount: NotRequired["str|None"]
            """
            ID of an existing discount on the object (or one of its ancestors) to reuse.
            """

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool
            """
            Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount_subtotal: int
    """
    Total before any discounts or taxes are applied.
    """
    amount_total: int
    """
    Total after discounts and taxes are applied.
    """
    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect Application that created the quote.
    """
    application_fee_amount: Optional[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Only applicable if there are no line items with recurring prices on the quote.
    """
    application_fee_percent: Optional[float]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. Only applicable if there are line items with recurring prices on the quote.
    """
    automatic_tax: StripeObject
    collection_method: Literal["charge_automatically", "send_invoice"]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    """
    computed: StripeObject
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: Optional[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
    """
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    """
    The tax rates applied to this quote.
    """
    description: Optional[str]
    """
    A description that will be displayed on the quote PDF.
    """
    discounts: List[ExpandableField["Discount"]]
    """
    The discounts applied to this quote.
    """
    expires_at: int
    """
    The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
    """
    footer: Optional[str]
    """
    A footer that will be displayed on the quote PDF.
    """
    from_quote: Optional[StripeObject]
    """
    Details of the quote that was cloned. See the [cloning documentation](https://stripe.com/docs/quotes/clone) for more details.
    """
    header: Optional[str]
    """
    A header that will be displayed on the quote PDF.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice: Optional[ExpandableField["Invoice"]]
    """
    The invoice that was created from this quote.
    """
    invoice_settings: Optional[StripeObject]
    """
    All invoices will be billed using the specified settings.
    """
    line_items: Optional[ListObject["LineItem"]]
    """
    A list of items the customer is being quoted for.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    number: Optional[str]
    """
    A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://stripe.com/docs/quotes/overview#finalize).
    """
    object: Literal["quote"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.
    """
    status: Literal["accepted", "canceled", "draft", "open"]
    """
    The status of the quote.
    """
    status_transitions: StripeObject
    subscription: Optional[ExpandableField["Subscription"]]
    """
    The subscription that was created or updated from this quote.
    """
    subscription_data: StripeObject
    subscription_schedule: Optional[ExpandableField["SubscriptionSchedule"]]
    """
    The subscription schedule that was created or updated from this quote.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this quote belongs to.
    """
    total_details: StripeObject
    transfer_data: Optional[StripeObject]
    """
    The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the invoices.
    """

    @classmethod
    def _cls_accept(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/accept".format(
                    quote=util.sanitize_id(quote)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def accept(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        ...

    @overload
    def accept(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        ...

    @class_method_variant("_cls_accept")
    def accept(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/accept".format(
                    quote=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_cancel(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/cancel".format(
                    quote=util.sanitize_id(quote)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def cancel(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/cancel".format(
                    quote=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.CreateParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_finalize_quote(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/finalize".format(
                    quote=util.sanitize_id(quote)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def finalize_quote(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        ...

    @overload
    def finalize_quote(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        ...

    @class_method_variant("_cls_finalize_quote")
    def finalize_quote(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/finalize".format(
                    quote=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListParams"]
    ) -> ListObject["Quote"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_computed_upfront_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/computed_upfront_line_items".format(
                    quote=util.sanitize_id(quote)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def list_computed_upfront_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        ...

    @overload
    def list_computed_upfront_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        ...

    @class_method_variant("_cls_list_computed_upfront_line_items")
    def list_computed_upfront_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/quotes/{quote}/computed_upfront_line_items".format(
                    quote=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_list_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/line_items".format(
                    quote=util.sanitize_id(quote)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def list_line_items(
        cls,
        quote: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        ...

    @overload
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/quotes/{quote}/line_items".format(
                    quote=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Quote.ModifyParams"]
    ) -> "Quote":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Quote",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Quote.RetrieveParams"]
    ) -> "Quote":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(sid),
            "pdf",
        )
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=stripe_version,
            account=stripe_account,
        )
        headers = util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @overload
    @classmethod
    def pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        ...

    @overload
    def pdf(
        self,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        ...

    @util.class_method_variant("_cls_pdf")
    def pdf(  # type: ignore
        self,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        version = api_version or stripe_version
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=version,
            account=stripe_account,
        )
        url = self.instance_url() + "/pdf"
        return requestor.request_stream("get", url, params=params)
