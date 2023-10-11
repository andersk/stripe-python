# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class CountrySpec(ListableAPIResource["CountrySpec"]):
    """
    Stripe needs to collect certain pieces of information about each account
    created. These requirements can differ depending on the account's country. The
    Country Specs API makes these rules available to your integration.

    You can also view the information from this API call as [an online
    guide](https://stripe.com/docs/connect/required-verification-information).
    """

    OBJECT_NAME = "country_spec"

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    default_currency: str
    id: str
    object: Literal["country_spec"]
    supported_bank_account_currencies: Dict[str, List[str]]
    supported_payment_currencies: List[str]
    supported_payment_methods: List[str]
    supported_transfer_countries: List[str]
    verification_fields: StripeObject

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CountrySpec.ListParams"]
    ) -> ListObject["CountrySpec"]:
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
    def retrieve(
        cls, id: str, **params: Unpack["CountrySpec.RetrieveParams"]
    ) -> "CountrySpec":
        instance = cls(id, **params)
        instance.refresh()
        return instance
