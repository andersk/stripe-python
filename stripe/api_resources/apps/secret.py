# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class Secret(CreateableAPIResource["Secret"], ListableAPIResource["Secret"]):
    """
    Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

    The primary resource in Secret Store is a `secret`. Other apps can't view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

    All Dashboard users and the app backend share `account` scoped secrets. Use the `account` scope for secrets that don't change per-user, like a third-party API key.

    A `user` scoped secret is accessible by the app backend and one specific Dashboard user. Use the `user` scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

    Related guide: [Store data between page reloads](https://stripe.com/docs/stripe-apps/store-auth-data-custom-objects)
    """

    OBJECT_NAME = "apps.secret"

    class CreateParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        expires_at: NotRequired[Optional[int]]
        name: str
        payload: str
        scope: "Secret.CreateScopeParams"

    class CreateScopeParams(TypedDict):
        type: Literal["account", "user"]
        user: NotRequired[Optional[str]]

    class DeleteWhereParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        name: str
        scope: "Secret.DeleteWhereScopeParams"

    class DeleteWhereScopeParams(TypedDict):
        type: Literal["account", "user"]
        user: NotRequired[Optional[str]]

    class FindParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        name: str
        scope: "Secret.FindScopeParams"

    class FindScopeParams(TypedDict):
        type: Literal["account", "user"]
        user: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        scope: "Secret.ListScopeParams"
        starting_after: NotRequired[Optional[str]]

    class ListScopeParams(TypedDict):
        type: Literal["account", "user"]
        user: NotRequired[Optional[str]]

    created: int
    deleted: Optional[bool]
    expires_at: Optional[int]
    id: str
    livemode: bool
    name: str
    object: Literal["apps.secret"]
    payload: Optional[str]
    scope: StripeObject

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Secret.CreateParams"]
    ) -> "Secret":
        return cast(
            "Secret",
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
    def delete_where(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Secret.DeleteWhereParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/apps/secrets/delete",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def find(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Secret.FindParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/apps/secrets/find",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Secret.ListParams"]
    ) -> ListObject["Secret"]:
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
