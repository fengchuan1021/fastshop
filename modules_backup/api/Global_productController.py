# generated timestamp: 2022-10-29T02:15:04+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .Global_productShema import (
    ApiProductGlobalProductsAttributesGetRequest,
    ApiProductGlobalProductsAttributesGetResponse,
    ApiProductGlobalProductsCategoriesGetResponse,
    ApiProductGlobalProductsCategoriesRulesGetRequest,
    ApiProductGlobalProductsCategoriesRulesGetResponse,
    ApiProductGlobalProductsDeleteRequest,
    ApiProductGlobalProductsDeleteResponse,
    ApiProductGlobalProductsPricesPutRequest,
    ApiProductGlobalProductsPricesPutResponse,
    ApiProductGlobalProductsPublishPostRequest,
    ApiProductGlobalProductsPublishPostResponse,
    ApiProductGlobalProductsSearchPostRequest,
    ApiProductGlobalProductsSearchPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="UpdateGlobalProductPrice put: /api/product/global_products/prices">
@router.put(
    '/api/product/global_products/prices',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsPricesPutResponse,
    
)
async def UpdateGlobalProductPrice(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    body: ApiProductGlobalProductsPricesPutRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdateGlobalProductPrice
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsPricesPutResponse()


# </editor-fold>


# <editor-fold desc="GetGlobalCategories get: /api/product/global_products/categories">
@router.get(
    '/api/product/global_products/categories',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsCategoriesGetResponse,
    
)
async def GetGlobalCategories(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetGlobalCategories
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsCategoriesGetResponse()


# </editor-fold>


# <editor-fold desc="DeleteGlobalProduct delete: /api/product/global_products">
@router.delete(
    '/api/product/global_products',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsDeleteResponse,
    
)
async def DeleteGlobalProduct(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiProductGlobalProductsDeleteRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    DeleteGlobalProduct
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsDeleteResponse()


# </editor-fold>


# <editor-fold desc="GetGlobalCategoryRule get: /api/product/global_products/categories/rules">
@router.get(
    '/api/product/global_products/categories/rules',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsCategoriesRulesGetResponse,
    
)
async def GetGlobalCategoryRule(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiProductGlobalProductsCategoriesRulesGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetGlobalCategoryRule
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsCategoriesRulesGetResponse()


# </editor-fold>


# <editor-fold desc="GetGlobalProductList post: /api/product/global_products/search">
@router.post(
    '/api/product/global_products/search',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsSearchPostResponse,
    
)
async def GetGlobalProductList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    body: ApiProductGlobalProductsSearchPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetGlobalProductList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsSearchPostResponse()


# </editor-fold>


# <editor-fold desc="PublishGlobalProduct post: /api/product/global_products/publish">
@router.post(
    '/api/product/global_products/publish',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsPublishPostResponse,
    
)
async def PublishGlobalProduct(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    body: ApiProductGlobalProductsPublishPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    PublishGlobalProduct
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsPublishPostResponse()


# </editor-fold>


# <editor-fold desc="GetGlobalAttributes get: /api/product/global_products/attributes">
@router.get(
    '/api/product/global_products/attributes',
    response_class=XTJsonResponse,
    response_model=ApiProductGlobalProductsAttributesGetResponse,
    
)
async def GetGlobalAttributes(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    body: ApiProductGlobalProductsAttributesGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetGlobalAttributes
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductGlobalProductsAttributesGetResponse()


# </editor-fold>
