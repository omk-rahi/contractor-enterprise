class AddExtraContextMixin:
    extra_context = {
        
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = self.extra_context
        return context
    
