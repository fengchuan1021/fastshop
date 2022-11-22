from sqlalchemy.orm import deferred, relationship, backref
import enum
from Models.ModelBase import Base,XTVARCHAR
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, TEXT, DECIMAL
from component.snowFlakeId import snowFlack
from typing import TYPE_CHECKING, List
from .Brand import Brand
if TYPE_CHECKING:
    from Models.product.VariantImage import VariantImage
    from .VariantShop import VariantShop
    from .Brand import Brand
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
    product_id = Column(BIGINT(20), primary_key=True, default=snowFlack.getId,comment="primary key")
    sku = Column(XTVARCHAR(80),comment="sku")

    brand_id =Column(INTEGER,index=True,server_default='0',default=0)

    brand_name= Column(XTVARCHAR(24), nullable=False, default='', server_default='')

    name_en= deferred(Column(XTVARCHAR(255),nullable=False,default='',server_default=''), group='en')
    description_en=deferred(Column(TEXT(),nullable=False,default=''), group='en')


    name_cn= deferred(Column(XTVARCHAR(255),nullable=False,default='',server_default=''), group='cn')
    description_cn=deferred(Column(TEXT(),nullable=False,default=''), group='cn')
    #brand_cn=deferred(Column(XTVARCHAR(24),nullable=False,default='',server_default=''), group='cn')

    useage_status=Column(ENUM("FRESHNEW","SECONDHAND","RETREAD"),server_default='FRESHNEW',default='FRESHNEW',comment="产品状态 全新 二手 翻新")
    tags=Column(XTVARCHAR(512),server_default='',default='',comment='product tag')
    measureunit=Column(ENUM(*[i.value for i in MeasureUnit]))
    referencevalue=Column(INTEGER,default=0,server_default='0',
                          comment='''参考值：将用于计算产品单价，并在产品页面展示产品单价
                           单价=（产品价格*参考值）/ 数量，详情查看<a href="https://merchantfaq.wish.com/hc/zh-cn/articles/4405383750555" target="_blank">后台说明</a>
                           例：<br>价格为15美元的产品，【计量单位】选择<b>毫升</b>，【参考值】<br>填写100，【数量值】填写200
                           单价展示<b>每100毫升的价格</b>，<br>单价=（15*100）/200=每100毫升7.5美元'''
                          )
    quantityvalue=Column(INTEGER,default=0,server_default='0',
                         comment='''数量值：每个产品包含多少单位的数量，用于计算产品单价
                            单价=（产品价格*参考值）/ 数量，详情查看<a href="https://merchantfaq.wish.com/hc/zh-cn/articles/4405383750555" target="_blank">后台说明</a>
                            例：<br>价格为15美元的产品，【计量单位】选择<b>毫升</b>，【参考值】<br>填写100，【数量值】填写200
                            单价展示<b>每100毫升的价格</b>，<br>单价=（15*100）/200=每100毫升7.5美元'''
                         )


    image=Column(XTVARCHAR(512),nullable=True,comment="product image.when any of variants are not chosed.can set as same as the defualt variant's fisrt image.")
    video=Column(XTVARCHAR(512),nullable=True)
    price=Column(DECIMAL(10,2))
    shipfee=Column(DECIMAL(10,2),default=0)
    stockqty=Column(INTEGER,default=0)
    msrp=Column(DECIMAL(10,2),default=0,comment="建议零售价")

    #海关物流信息 可以单独创建一个表
    hscode=Column(XTVARCHAR(64),default='')
    weight=Column(INTEGER,default=0,comment='重量 单位g')
    declarename=Column(XTVARCHAR(32),default='',comment='海关申报名称')
    declarelocalname=Column(XTVARCHAR(32),default='',comment='以原产国当地语言申报的名称')
    packlength=Column(INTEGER,default=0,comment='包裹长 单位cm')
    packwidth=Column(INTEGER,default=0,comment='包裹宽 单位cm')
    packheight=Column(INTEGER,default=0,comment='包裹高 单位cm')
    declarevalue=Column(DECIMAL(10,2),default=0,comment='申报价值')
    numbers=Column(INTEGER,default=0,comment='数量')
    shipfromcountry=Column(INTEGER,index=True,comment='发货国家/地区')
    hasdust=Column(ENUM("N","Y"),default='N',comment="含有粉末")
    hasliquid=Column(ENUM("N","Y"),default='N',comment="含有液体")
    hasbettory=Column(ENUM("N","Y"),default='N',comment="含有电池")
    hasmetal=Column(ENUM("N","Y"),default='N',comment="含有金属")

    #变体
    variantcolours_en=Column(XTVARCHAR(128),default='',comment="拥有的变体的颜色。如:红色,蓝色,绿色")
    variantsizes_en = Column(XTVARCHAR(128), default='',comment="拥有的变体的颜色。如:X,XL,XXL")
    variantcolours_cn=Column(XTVARCHAR(128),default='',comment="拥有的变体的颜色。如:红色,蓝色,绿色")
    variantsizes_cn = Column(XTVARCHAR(128), default='',comment="拥有的变体的颜色。如:X,XL,XXL")


    Variant:List['Variant']=relationship('Variant',uselist=True, primaryjoin='foreign(Product.product_id) == Variant.product_id',back_populates='Product')

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
    sku=Column(XTVARCHAR(80))

    product_id=Column(BIGINT,server_default="0")
    #price = Column(DECIMAL(10,2), server_default="0",default=0)

    specification_en=Column(XTVARCHAR(12),server_default='')
    specification_cn = Column(XTVARCHAR(12), server_default='')

    color_en=Column(XTVARCHAR(12), server_default='')
    color_cn = Column(XTVARCHAR(12), server_default='')

    image=Column(XTVARCHAR(512),nullable=True,comment="")

    brand_id=Column(INTEGER,default=0,server_default="0")
    brand_name=Column(XTVARCHAR(24),nullable=True)

    name_en= deferred(Column(XTVARCHAR(255),nullable=True), group='en')
    name_cn= deferred(Column(XTVARCHAR(255),nullable=True), group='cn')

    Product:Product=relationship("Product",uselist=False,primaryjoin='foreign(Product.product_id)==Variant.variant_id',back_populates='Variant')
    #dynamic:"ProductDynamic" = relationship(ProductDynamic, uselist=False, backref="product_static")
    VariantImage:List['VariantImage'] = relationship('VariantImage',uselist=True,

                                               primaryjoin='foreign(Variant.variant_id) == VariantImage.variant_id')


    VariantShop:List['VariantShop']=relationship('VariantShop',uselist=True,
                                           primaryjoin='foreign(Variant.variant_id) == VariantShop.variant_id',
                                           back_populates='Variant'
                                           )
