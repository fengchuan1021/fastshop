from sqlalchemy.orm import deferred, relationship, backref
import enum
from Models.ModelBase import Base, XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, TEXT, DECIMAL, DATETIME
from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from Models import VariantImage, VariantStore, ProductAttribute, ProductSpecification, ProductCategory, Merchant, \
        Store, SupplierVariant, VariantWarehouse, PurchaseReceiptItems


class MeasureUnit(enum.Enum):
    OUNCE = "OUNCE"  # oz（盎司）
    POUND = "POUND"  # lb（磅）
    GRAM = "GRAM"  # g（克）
    MILLIGRAM = "MILLIGRAM"  # mg（毫克）
    KILOGRAM = "KILOGRAM"  # kg（千克）
    FLUID_OUNCE = "FLUID_OUNCE"  # floz（液量盎司）
    PINT = "PINT"  # pt（品脱）
    QUART = "QUART"  # qt（夸脱）
    GALLON = "GALLON"  # gal（加仑）
    MILLILITER = "MILLILITER"  # ml（毫升）
    CENTILITER = "CENTILITER"  # cl（厘升）
    LITER = "LITER"  # l（升）
    CUBICMETER = "CUBICMETER"  # cbm（立方米）
    INCH = "INCH"  # in（英寸）
    FOOT = "FOOT"  # ft（英尺）
    YARD = "YARD"  # yd（码）
    CENTIMETER = "CENTIMETER"  # cm（厘米）
    METER = "METER"  # m（米）
    SQUARE_FOOT = "SQUARE_FOOT"  # sqft（平方英尺）
    SQUARE_METER = "SQUARE_METER"  # sqm（平方米）
    COUNT = "COUNT"  # count（件）
    LOAD = "LOAD"  # load（缸）
    WASH = "WASH"  # wash（次）
    ROLL = "ROLL"  # roll（卷）
    POD = "POD"  # pod（包）


class Product(Base):
    __tablename__ = 'product'
    product_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId, comment="primary key")
    sku = Column(XTVARCHAR(80), comment="sku")

    brand_id = Column(INTEGER, index=True, server_default='0', default=0)
    brand_name = Column(XTVARCHAR(24), nullable=False, default='', server_default='')

    title = Column(XTVARCHAR(255), nullable=False, default='', server_default='')
    description = Column(TEXT(), nullable=False, default='')

    # name_cn= deferred(Column(XTVARCHAR(255),nullable=False,default='',server_default=''), group='cn')
    # description_cn=deferred(Column(TEXT(),nullable=False,default=''), group='cn')
    # brand_cn=deferred(Column(XTVARCHAR(24),nullable=False,default='',server_default=''), group='cn')

    useage_status = Column(ENUM("NEW", "USED", "REFURBISHED"), server_default='NEW', default='NEW',
                           comment="产品状态 全新 二手 翻新")
    tags = Column(XTVARCHAR(512), server_default='', default='', comment='product tag')
    measureunit = Column(ENUM(*[i.value for i in MeasureUnit]))

    '''参考值：将用于计算产品单价，并在产品页面展示产品单价
                           单价=（产品价格*参考值）/ 数量，详情查看<a href="https://merchantfaq.wish.com/hc/zh-cn/articles/4405383750555" target="_blank">后台说明</a>
                           例：<br>价格为15美元的产品，【计量单位】选择<b>毫升</b>，【参考值】<br>填写100，【数量值】填写200
                           单价展示<b>每100毫升的价格</b>，<br>单价=（15*100）/200=每100毫升7.5美元'''
    referencevalue = Column(INTEGER, default=0, server_default='0',
                            comment=''
                            )

    '''数量值：每个产品包含多少单位的数量，用于计算产品单价
                                单价=（产品价格*参考值）/ 数量，详情查看<a href="https://merchantfaq.wish.com/hc/zh-cn/articles/4405383750555" target="_blank">后台说明</a>
                                例：<br>价格为15美元的产品，【计量单位】选择<b>毫升</b>，【参考值】<br>填写100，【数量值】填写200
                                单价展示<b>每100毫升的价格</b>，<br>单价=（15*100）/200=每100毫升7.5美元'''
    quantityvalue = Column(INTEGER, default=0, server_default='0',
                           comment=''
                           )

    image = Column(XTVARCHAR(512), nullable=True,
                   comment="product image.when any of variants are not chosed.can set as same as the defualt variant's fisrt image.")
    video = Column(XTVARCHAR(512), nullable=True)
    price = Column(DECIMAL(10, 2))
    shipfee = Column(DECIMAL(10, 2), default=0)
    # stockqty=Column(INTEGER,default=0)
    msrp = Column(DECIMAL(10, 2), default=0, comment="建议零售价")

    # 海关物流信息 可以单独创建一个表
    hscode = Column(XTVARCHAR(64), default='')
    weight = Column(INTEGER, default=0, comment='重量 单位g')
    declarename = Column(XTVARCHAR(32), default='', comment='海关申报名称')
    declarelocalname = Column(XTVARCHAR(32), default='', comment='以原产国当地语言申报的名称')
    packlength = Column(INTEGER, default=0, comment='包裹长 单位cm')
    packwidth = Column(INTEGER, default=0, comment='包裹宽 单位cm')
    packheight = Column(INTEGER, default=0, comment='包裹高 单位cm')
    declarevalue = Column(DECIMAL(10, 2), default=0, comment='申报价值')
    numbers = Column(INTEGER, default=0, comment='数量')
    shipfromcountry = Column(INTEGER, index=True, comment='发货国家/地区')
    hasdust = Column(ENUM("N", "Y"), default='N', comment="含有粉末")
    hasliquid = Column(ENUM("N", "Y"), default='N', comment="含有液体")
    hasbettory = Column(ENUM("N", "Y"), default='N', comment="含有电池")
    hasmetal = Column(ENUM("N", "Y"), default='N', comment="含有金属")

    # 变体 优化常用的颜色尺寸为固定列
    specificationcolours = Column(XTVARCHAR(128), default='', comment="拥有的变体的颜色。如:红色,蓝色,绿色")
    specificationsizes = Column(XTVARCHAR(128), default='', comment="拥有的变体的颜色。如:X,XL,XXL")
    specification = Column(XTVARCHAR(255), default='', comment="除颜色尺寸外剩余的规格")
    # 多语言
    language = Column(ENUM('en', "cn"), default='en', comment="语言，XT内部使用")
    en_product_id = Column(BIGINT, default=0, index=True, comment="语言如果是非en,指向原en产品")

    Variant: List['Variant'] = relationship('Variant', uselist=True,
                                            primaryjoin='foreign(Variant.product_id) == Product.product_id',
                                            back_populates='Product', cascade='delete')

    ProductAttribute: List['ProductAttribute'] = relationship('ProductAttribute', uselist=True,
                                                              primaryjoin='foreign(ProductAttribute.product_id) == Product.product_id',
                                                              back_populates='Product', cascade='')

    ProductSpecification: List['ProductSpecification'] = relationship('ProductSpecification', uselist=True,
                                                                      primaryjoin='foreign(ProductSpecification.product_id) == Product.product_id',
                                                                      back_populates='Product', cascade='')
    ProductCategory: List['ProductCategory'] = relationship('ProductCategory', uselist=True,
                                                            primaryjoin='foreign(ProductCategory.product_id)==Product.product_id',
                                                            back_populates='Product', cascade='')
    merchant_id = Column(INTEGER, index=True)
    # store_id=Column(INTEGER,index=True)
    Merchant: 'Merchant' = relationship('Merchant', uselist=False,
                                        primaryjoin='foreign(Product.merchant_id) == Merchant.merchant_id',
                                        back_populates='Product', cascade='')
    # Store:'Store'=relationship('Store', uselist=False,
    #                        primaryjoin='foreign(Product.store_id) == Store.store_id',
    #                        back_populates='Product',cascade='')

    VariantStore: List['VariantStore'] = relationship('VariantStore', uselist=True,
                                                      primaryjoin='foreign(VariantStore.product_id) == Product.product_id',
                                                      back_populates='Product', cascade=''
                                                      )


# class VariantStatis(Base):
#     '''for statistics'''
#     __tablename__ = 'variant_Statis'
#     variant_Statis_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
#     is_hot=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
#     is_recommend=Column(ENUM("TRUE","FALSE"),server_default="FALSE",default="FALSE",index=True)
#     collect_cnt=Column(INTEGER,server_default="0",default="0",index=True)
#     sale_cnt=Column(INTEGER,server_default="0",default="0",index=True)
#     stock=Column(INTEGER,server_default="0")

class Variant(Base):
    __tablename__ = 'variant'
    variant_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
    sku = Column(XTVARCHAR(80))

    product_id = Column(BIGINT, server_default="0", index=True)
    # price = Column(DECIMAL(10,2), server_default="0",default=0)

    qty = Column(INTEGER, default=0, server_default='0', index=True)

    specification = Column(XTVARCHAR(12), server_default='')

    color = Column(XTVARCHAR(12), server_default='')
    size = Column(XTVARCHAR(12), server_default='')

    image = Column(XTVARCHAR(512), nullable=True, comment="")

    brand_id = Column(INTEGER, default=0, server_default="0")
    brand_name = Column(XTVARCHAR(24), nullable=True)

    title = Column(XTVARCHAR(255), nullable=True)

    Product: Product = relationship("Product", uselist=False,
                                    primaryjoin='foreign(Variant.product_id)==Product.product_id',
                                    back_populates='Variant', cascade='')
    # dynamic:"ProductDynamic" = relationship(ProductDynamic, uselist=False, backref="product_static")
    PurchaseReceiptItems: List['PurchaseReceiptItems'] = relationship('PurchaseReceiptItems',
                                                                      primaryjoin='foreign(PurchaseReceiptItems.variant_id) == Variant.variant_id',
                                                                      uselist=True, back_populates='Variant',
                                                                      cascade='')
    VariantImage: List['VariantImage'] = relationship('VariantImage', uselist=True,

                                                      primaryjoin='foreign(VariantImage.variant_id) == Variant.variant_id',
                                                      cascade='delete')

    VariantStore: List['VariantStore'] = relationship('VariantStore', uselist=True,
                                                      primaryjoin='foreign(VariantStore.variant_id) == Variant.variant_id',
                                                      back_populates='Variant', cascade=''
                                                      )

    merchant_id = Column(INTEGER, index=True)
    store_id = Column(INTEGER, index=True)
    Merchant: 'Merchant' = relationship('Merchant', uselist=False,
                                        primaryjoin='foreign(Variant.merchant_id) == Merchant.merchant_id',
                                        back_populates='Variant', cascade='')
    Store: 'Store' = relationship('Store', uselist=False,
                                  primaryjoin='foreign(Variant.store_id) == Store.store_id',
                                  back_populates='Variant', cascade='')

    SupplierVariant: List['SupplierVariant'] = relationship('SupplierVariant',
                                                            primaryjoin="foreign(SupplierVariant.variant_id)==Variant.variant_id",
                                                            cascade='', back_populates='Variant')

    # VariantWarehouse:List['VariantWarehouse']=relationship('VariantWarehouse',uselist=True,
    #                                                        primaryjoin='foreign(VariantWarehouse.variant_id) ==Variant.variant_id',
    #                                                        back_populates='Variant', cascade=''
    #                                                        )


# class WishProduct(Base):
#     __tablename__ = 'wish_product'
#     wish_product_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId)
#     status = Column(
#         ENUM("PENDING_REVIEW", "APPROVED", "REJECTED", "REMOVED_BY_WISH", "REMOVED_BY_MERCHANT"),
#         server_default='PENDING_REVIEW', default='PENDING_REVIEW',
#         comment="待审查 / 通过 / 拒绝 / 被wish移除 / 被商家移除")
#     created_at = Column(DATETIME)
#     updated_at = Column(DATETIME)
#     description = Column(TEXT)
#     tags = Column(XTVARCHAR(512), nullable=True, comment="")
#     subcategory_id = Column(INTEGER, default=0, comment="")
#     num_saves = Column(INTEGER, default=0, comment="")
#     category_experience_eligibility = Column(ENUM("TURE", "FALSE"))
#     num_sold = Column(INTEGER, default=0, comment="")
#     parent_sku = Column(XTVARCHAR(512), nullable=True, comment="")
#     wish_id = Column(XTVARCHAR(256), nullable=True, comment="")
#     name = Column(XTVARCHAR(512), nullable=True, comment="")
