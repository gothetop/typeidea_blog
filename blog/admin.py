from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Post, Category, Tag
from blog.adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):    # 可以选择继承自admin.StackedInline以获取不同的展示样式
    fields = ("title", "desc", "status")
    extra = 1  # 控制额外多几个
    model = Post


# liushijia   root050513
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]    # 在分类页面也可以编辑文章了

    list_display = ("name", "status", "is_nav", "created_time", "owner", "post_count")
    fields = ("name", "status", "is_nav")

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = "文章数量"


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ("name", "status", "created_time", "owner")
    fields = ("name", "status")


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""

    title = "分类过滤器"   # 展示标题
    parameter_name= "owner_category"    # 查询时URL参数的名字

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list("id", "name")

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        "title", "category", "tag", "status",
        "created_time", "owner", "operator"
    ]
    list_display_links = ["title"]   # list_display_links  用来配置那些字段可以作为链接，点击他们，可以进入编辑页面

    # list_filter = ["category", "tag"]    # 配置页面过滤器 需要通过那些字段来过滤列表页  右边的过滤列表
    # 自定义过滤器
    list_filter = [CategoryOwnerFilter]
    search_fields = ["title", "category__name"]  # 配置搜索字段   可以用过搜索栏输入该字段来搜索

    actions_on_top = True     # 动作相关的配置是否展示在顶部
    actions_on_bottom = False    # 动作相关的配置是否展示在底部

    # 编辑页面
    save_on_top = False     # 保存、编辑、编辑并新建按钮是否在顶部展示

    exclude = ["owner"]
    # fields配置
    # fields = (
    #     ("category", "title"),
    #     "desc",
    #     "status",
    #     "context",
    #     "tag",
    # )

    # fieldsets配置  用来控制页面布局
    fieldsets = (
        ("基础配置", {
            "description": "基础配置描述",
            "fields": (
                ("title", "category"),
                "status",
            ),
        }),
        ("内容", {
            "fields": (
                "desc",
                "context",
            ),
        }),
        ("额外信息", {
            "classes": ("collapse",),
            "fields": ("tag", ),
        }),
    )
    # filter_horizontal = ("tag", )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:blog_post_change", args=(obj.id,))
        )
    operator.short_description = "操作"    # 指定表头的展示文案


    # class Media:
    #     css = {
    #         "all": ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js", )


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ["object_repr", "object_id", "action_flag", "user", "change_message"]




