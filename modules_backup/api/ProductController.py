# generated timestamp: 2022-10-29T02:15:03+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .ProductShema import (
    ApiProductsActivatePostRequest,
    ApiProductsActivatePostResponse,
    ApiProductsAttributesGetRequest,
    ApiProductsAttributesGetResponse,
    ApiProductsBrandsGetRequest,
    ApiProductsBrandsGetResponse,
    ApiProductsCategoriesGetResponse,
    ApiProductsCategoriesRulesGetRequest,
    ApiProductsCategoriesRulesGetResponse,
    ApiProductsDetailsGetRequest,
    ApiProductsDetailsGetResponse,
    ApiProductsInactivatedProductsPostRequest,
    ApiProductsInactivatedProductsPostResponse,
    ApiProductsPricesPutRequest,
    ApiProductsPricesPutResponse,
    ApiProductsPutRequest,
    ApiProductsPutResponse,
    ApiProductsRecoverPostRequest,
    ApiProductsRecoverPostResponse,
    ApiProductsSearchPostRequest,
    ApiProductsSearchPostResponse,
    ApiProductsStocksPutRequest,
    ApiProductsStocksPutResponse,
    ApiProductsUploadFilesPostRequest,
    ApiProductsUploadFilesPostResponse,
    ApiProductsUploadImgsPostRequest,
    ApiProductsUploadImgsPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="GetCategoryRule get: /api/products/categories/rules">
@router.get(
    '/api/products/categories/rules',
    response_class=XTJsonResponse,
    response_model=ApiProductsCategoriesRulesGetResponse,
    
)
async def GetCategoryRule(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsCategoriesRulesGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetCategoryRule
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsCategoriesRulesGetResponse()


# </editor-fold>


# <editor-fold desc="RecoverDeletedProduct post: /api/products/recover">
@router.post(
    '/api/products/recover',
    response_class=XTJsonResponse,
    response_model=ApiProductsRecoverPostResponse,
    
)
async def RecoverDeletedProduct(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsRecoverPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    RecoverDeletedProduct
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsRecoverPostResponse()


# </editor-fold>


# <editor-fold desc="GetBrands get: /api/products/brands">
@router.get(
    '/api/products/brands',
    response_class=XTJsonResponse,
    response_model=ApiProductsBrandsGetResponse,
    
)
async def GetBrands(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsBrandsGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetBrands
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsBrandsGetResponse()


# </editor-fold>


# <editor-fold desc="ActivateProduct post: /api/products/activate">
@router.post(
    '/api/products/activate',
    response_class=XTJsonResponse,
    response_model=ApiProductsActivatePostResponse,
    
)
async def ActivateProduct(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsActivatePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    ActivateProduct
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsActivatePostResponse()


# </editor-fold>


# <editor-fold desc="GetCategories get: /api/products/categories">
@router.get(
    '/api/products/categories',
    response_class=XTJsonResponse,
    response_model=ApiProductsCategoriesGetResponse,
    
)
async def GetCategories(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetCategories
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsCategoriesGetResponse()


# </editor-fold>


# <editor-fold desc="GetProductList post: /api/products/search">
@router.post(
    '/api/products/search',
    response_class=XTJsonResponse,
    response_model=ApiProductsSearchPostResponse,
    
)
async def GetProductList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsSearchPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetProductList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsSearchPostResponse()


# </editor-fold>


# <editor-fold desc="GetProductDetail get: /api/products/details">
@router.get(
    '/api/products/details',
    response_class=XTJsonResponse,
    response_model=ApiProductsDetailsGetResponse,
    
)
async def GetProductDetail(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsDetailsGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetProductDetail
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsDetailsGetResponse()


# </editor-fold>


# <editor-fold desc="EditProduct put: /api/products">
@router.put(
    '/api/products',
    response_class=XTJsonResponse,
    response_model=ApiProductsPutResponse,
    
)
async def EditProduct(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsPutRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    EditProduct
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsPutResponse()


# </editor-fold>


# <editor-fold desc="UpdateStock put: /api/products/stocks">
@router.put(
    '/api/products/stocks',
    response_class=XTJsonResponse,
    response_model=ApiProductsStocksPutResponse,
    
)
async def UpdateStock(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsStocksPutRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdateStock
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsStocksPutResponse()


# </editor-fold>


# <editor-fold desc="GetAttributes get: /api/products/attributes">
@router.get(
    '/api/products/attributes',
    response_class=XTJsonResponse,
    response_model=ApiProductsAttributesGetResponse,
    
)
async def GetAttributes(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsAttributesGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetAttributes
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsAttributesGetResponse()


# </editor-fold>


# <editor-fold desc="UploadImage post: /api/products/upload_imgs">
@router.post(
    '/api/products/upload_imgs',
    response_class=XTJsonResponse,
    response_model=ApiProductsUploadImgsPostResponse,
    
)
async def UploadImage(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    shop_id: str = ...,
    body: ApiProductsUploadImgsPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UploadImage
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsUploadImgsPostResponse()


# </editor-fold>


# <editor-fold desc="DeactivateProduct post: /api/products/inactivated_products">
@router.post(
    '/api/products/inactivated_products',
    response_class=XTJsonResponse,
    response_model=ApiProductsInactivatedProductsPostResponse,
    
)
async def DeactivateProduct(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsInactivatedProductsPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    DeactivateProduct
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsInactivatedProductsPostResponse()


# </editor-fold>


# <editor-fold desc="UpdatePrice put: /api/products/prices">
@router.put(
    '/api/products/prices',
    response_class=XTJsonResponse,
    response_model=ApiProductsPricesPutResponse,
    
)
async def UpdatePrice(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiProductsPricesPutRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdatePrice
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsPricesPutResponse()


# </editor-fold>


# <editor-fold desc="UploadFile post: /api/products/upload_files">
@router.post(
    '/api/products/upload_files',
    response_class=XTJsonResponse,
    response_model=ApiProductsUploadFilesPostResponse,
    
)
async def UploadFile(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiProductsUploadFilesPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UploadFile
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiProductsUploadFilesPostResponse()


# </editor-fold>
