from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onlineversion.views.home', name='home'),
    # url(r'^onlineversion/', include('onlineversion.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #index
    url(r'^index$', 'versiononline.index.index_view',name='index_view'),

    #ead_online_version
    url(r'^ead_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^ead_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^ead_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^product_save', 'versiononline.onlineversion_info.save_product',name='save_product'),

    url(r'^ead_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),
    url(r'^product_add_save', 'versiononline.onlineversion_info.product_add_save',name='product_add_save'),


    url(r'^delete_productSet', 'versiononline.onlineversion_info.delete_productSet',name='delete_productSet'),


    #search_online_version
    url(r'^search_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^search_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^search_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^search_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),

    #armani_online_version
    url(r'^armani_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^armani_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^armani_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^armani_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),

    #infra_online_version
    url(r'^infra_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^infra_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^infra_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^infra_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),

    #YNote_online_version
    url(r'^YNote_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^YNote_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^YNote_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^YNote_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),

    #dict_online_version
    url(r'^dict_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^dict_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^dict_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^dict_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),

    #fanyi_online_version
    url(r'^fanyi_online_version$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),
    url(r'^fanyi_online_version/\d+$', 'versiononline.onlineversion_info.onlineversion_info',name='onlineversion_info'),

    url(r'^fanyi_online_version/product_edit/\d+', 'versiononline.onlineversion_info.edit_product',name='edit_product'),
    url(r'^fanyi_online_version/\d+/product_add', 'versiononline.onlineversion_info.add_product_view',name='add_product_view'),
)
