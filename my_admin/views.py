from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View


from services.models import Service

from shop.models import Brand, ProductType, Category, Product, ProductImage, Specification

from accounts.models import CustomUser

from accounts.forms import StaffRegisterForm


# Create your views here.


class AddExtraContextMixin:
    extra_context = {
        
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = self.extra_context
        return context
    



# DASHBOARD

class DashBoardView(TemplateView):
    template_name = "my_admin/dashboard.html"


# SERVICES

class ServicesOverview(TemplateView):
    template_name = "my_admin/services-overview.html"
    

class ListServiceView(AddExtraContextMixin, ListView):
    model = Service
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Services",
        "fields": [field.name for field in Service._meta.get_fields() if not field.is_relation]
    }


class CreateServiceView(AddExtraContextMixin, CreateView):
    model = Service
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Service"
    }

class UpdateServiceView(AddExtraContextMixin, UpdateView):
    model = Service
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Service"
    }

class DeleteServiceView(AddExtraContextMixin, DeleteView):
    model = Service
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-service')

    extra_context = {
        "title": "Service"
    }








# SHOP

class ShopOverview(TemplateView):
    template_name = "my_admin/shop-overview.html"


# BRANDS

class ListBrandView(AddExtraContextMixin, ListView):
    model = Brand
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Brands",
        "fields": [field.name for field in Brand._meta.get_fields() if not field.is_relation]
    }


class CreateBrandView(AddExtraContextMixin, CreateView):
    model = Brand
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-brand')

    extra_context = {
        "title": "Brand"
    }

class UpdateBrandView(AddExtraContextMixin, UpdateView):
    model = Brand
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-brand')

    extra_context = {
        "title": "Brand"
    }

class DeleteBrandView(AddExtraContextMixin, DeleteView):
    model = Brand
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-brand')

    extra_context = {
        "title": "Brand"
    }

# Product Types

class ListProductTypeView(AddExtraContextMixin, ListView):
    model = ProductType
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Product Types",
        "fields": [field.name for field in ProductType._meta.get_fields() if not field.is_relation]
    }


class CreateProductTypeView(AddExtraContextMixin, CreateView):
    model = ProductType
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product-type')

    extra_context = {
        "title": "Product Type"
    }

class UpdateProductTypeView(AddExtraContextMixin, UpdateView):
    model = ProductType
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product-type')

    extra_context = {
        "title": "Product Type"
    }

class DeleteProductTypeView(AddExtraContextMixin, DeleteView):
    model = ProductType
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-product-type')

    extra_context = {
        "title": "Product Type"
    }


# Category


class ListCategoryView(AddExtraContextMixin, ListView):
    model = Category
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Categories",
        "fields": [field.name for field in Category._meta.get_fields() if not field.is_relation]
    }


class CreateCategoryView(AddExtraContextMixin, CreateView):
    model = Category
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-category')

    extra_context = {
        "title": "Category"
    }

class UpdateCategoryView(AddExtraContextMixin, UpdateView):
    model = Category
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-category')

    extra_context = {
        "title": "Category"
    }

class DeleteCategoryView(AddExtraContextMixin, DeleteView):
    model = Category
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-category')

    extra_context = {
        "title": "Category"
    }


# Product

class ListProductView(AddExtraContextMixin, ListView):
    model = Product
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Products",
        "fields": [field.name for field in Product._meta.get_fields() if not field.is_relation],
        "allow_view_detail": True
    }


class DetailProductView(AddExtraContextMixin, DetailView):
    model = Product
    template_name = "my_admin/product-detail.html"



class CreateProductView(AddExtraContextMixin, CreateView):
    model = Product
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Product"
    }

class UpdateProductView(AddExtraContextMixin, UpdateView):
    model = Product
    template_name = "my_admin/update-template.html"
    fields = "__all__"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Product"
    }

class DeleteProductView(AddExtraContextMixin, DeleteView):
    model = Product
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-product')

    extra_context = {
        "title": "Product"
    }



# PRODUCT IMAGES

class ListProductImageView(AddExtraContextMixin, ListView):
    model = ProductImage
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Product Images",
        "fields": [field.name for field in ProductImage._meta.get_fields() if not field.is_relation]
    }


class CreateProductImageView(AddExtraContextMixin, CreateView):
    model = ProductImage
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    

    extra_context = {
        "title": "Product Image"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-image', kwargs={'product_pk': self.kwargs["product_pk"]})
    
    
class UpdateProductImageView(AddExtraContextMixin, UpdateView):
    model = ProductImage
    template_name = "my_admin/update-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Product Image"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-image', kwargs={'product_pk': self.kwargs["product_pk"]})
    

class DeleteProductImageView(AddExtraContextMixin, DeleteView):
    model = ProductImage
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Product Image"
    }

    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-image', kwargs={'product_pk': self.kwargs["product_pk"]})
    

# PRODUCT SPECS

class ListProductSpecsView(AddExtraContextMixin, ListView):
    model = Specification
    template_name = "my_admin/list-template.html"
    paginate_by = 5 
    extra_context = {
        "title": "Product Specs",
        "fields": [field.name for field in Specification._meta.get_fields() if not field.is_relation]
    }


class CreateProductSpecsView(AddExtraContextMixin, CreateView):
    model = Specification
    template_name = "my_admin/create-template.html"
    fields = "__all__"
    

    extra_context = {
        "title": "Product Specs"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})
    
    
class UpdateProductSpecsView(AddExtraContextMixin, UpdateView):
    model = Specification
    template_name = "my_admin/update-template.html"
    fields = "__all__"

    extra_context = {
        "title": "Product Specs"
    }

    def get_initial(self):
        initial = super().get_initial()

        initial["product"] = self.kwargs["product_pk"]

        return initial
    
    
    def form_valid(self, form):
        
        form.instance.product = Product.objects.get(id = self.kwargs["product_pk"])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})
    

class DeleteProductSpecsView(AddExtraContextMixin, DeleteView):
    model = Specification
    template_name = "my_admin/delete-template.html"

    extra_context = {
        "title": "Product Specs"
    }

    
    def get_success_url(self):
        return reverse_lazy('admin/list-product-spec', kwargs={'product_pk': self.kwargs["product_pk"]})




# CUSTOMER

class ListCustomerView(View):
    def get(self, request):

        object_list = CustomUser.objects.filter(role='customer')

        extra = {
            "title": "Customers",
            "fields" : ["id", "fullname", "email", "phone"],
            "not_allow_action": True
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 


class ListStaffView(View):
    def get(self, request):

        object_list = CustomUser.objects.filter(role='staff')

        extra = {
            "title": "Staffs",
            "fields" : ["id", "fullname", "email", "phone"],
        }

        return render(request, "my_admin/list-template.html", context={"object_list": object_list, "extra" : extra}) 


class CreateStaffView(AddExtraContextMixin, CreateView):
    model = CustomUser
    form_class = StaffRegisterForm
    template_name = "my_admin/create-template.html"
    success_url = reverse_lazy('admin/list-staff')

    extra_context = {
        "title": "Staff"
    }

class UpdateStaffView(AddExtraContextMixin, UpdateView):
    model = CustomUser
    template_name = "my_admin/update-template.html"
    form_class = StaffRegisterForm
    success_url = reverse_lazy('admin/list-staff')

    extra_context = {
        "title": "Staff"
    }

class DeleteStaffView(AddExtraContextMixin, DeleteView):
    model = CustomUser
    template_name = "my_admin/delete-template.html"
    success_url = reverse_lazy('admin/list-staff')

    extra_context = {
        "title": "Staff"
    }



class UpdateAdminView(AddExtraContextMixin, UpdateView):
    model = CustomUser
    template_name = "my_admin/update-template.html"
    fields = ["fullname", "email", "phone",]
    success_url = reverse_lazy('admin/dashboard')

    extra_context = {
        "title": "Settings"
    }

    def get_object(self):
        # Return the profile of the currently logged-in user
        return self.request.user