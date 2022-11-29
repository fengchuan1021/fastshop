import enum
class UserRole(enum.Enum):
    '''一个注册用户只有一个角色 如果想要用户拥有多个角色 就添加一个新角色 定义新角色的权限为多个角色的权限'''
    customer=0#普通消费者
    root=1#管理员
    merchant=2#商家

