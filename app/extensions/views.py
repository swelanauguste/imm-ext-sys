from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import FormView

from .forms import (
    EnquiryCreateForm,
    EnquiryPaymentCreateForm,
    EnquiryRemarksCreateForm,
    SubsequentPermitCreateForm,
    SubsequentPermitPaymentCreateForm,
    SubsequentPermitPaymentUpdateForm,
)
from .models import (
    Enquiry,
    EnquiryPayment,
    EnquiryRemark,
    IndividualArrears,
    SubsequentPermit,
    SubsequentPermitPayment,
    SubsequentPermitRemark,
)


class EnquiryPaymentDetailView(LoginRequiredMixin, DetailView):
    model = EnquiryPayment


class EnquiryPaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = EnquiryPayment
    form_class = EnquiryPaymentCreateForm

    def get_initial(self):
        enquiry_id = self.kwargs["pk"]
        enquiry = get_object_or_404(Enquiry, pk=enquiry_id)
        return {"enquiry": enquiry, "payment_amount": enquiry.get_enquiry_cost()}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class SubsequentPermitPaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = SubsequentPermitPayment
    form_class = SubsequentPermitPaymentUpdateForm


# class SubsequentPermitPaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = SubsequentPermitPayment
#     form_class = SubsequentPermitPaymentCreateForm

#     def get_initial(self):


class SubsequentPermitDetailView(LoginRequiredMixin, DetailView):
    model = SubsequentPermit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_form"] = SubsequentPermitPaymentCreateForm(
            initial={
                "subsequent_permit": self.object,
                "payment_amount": self.object.get_subsequent_permit_cost(),
            }
        )
        # context["subsequent_permit_form"] = SubsequentPermitCreateForm(
        #     initial={"enquiry": self.object}
        # )
        return context


class SubsequentPermitCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SubsequentPermit
    form_class = SubsequentPermitCreateForm

    def get_initial(self):
        enquiry_id = self.kwargs["enquiry_id"]
        enquiry = get_object_or_404(Enquiry, pk=enquiry_id)
        return {"enquiry": enquiry, "granted_by": self.request.user}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        form.instance.granted_by = self.request.user
        return super().form_valid(form)


class SubsequentPermitListView(LoginRequiredMixin, ListView):
    model = SubsequentPermit


class SubsequentPermitUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SubsequentPermit


class EnquiryRemarksCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = EnquiryRemark
    form_class = EnquiryRemarksCreateForm


class EnquiryListView(LoginRequiredMixin, ListView):
    model = Enquiry

    def get_queryset(self):
        query = self.request.GET.get("enquiries")
        if query:
            return Enquiry.objects.filter(
                Q(surname__icontains=query)
                | Q(christian_names__icontains=query)
                | Q(pob__icontains=query)
                | Q(nationality__icontains=query)
                | Q(foreign_address__icontains=query)
                | Q(foreign_address1__icontains=query)
                | Q(phone__icontains=query)
                | Q(email__icontains=query)
                | Q(occu__icontains=query)
                | Q(marital_status__name__icontains=query)
                | Q(ppn__icontains=query)
                | Q(pp_issue_place__icontains=query)
                | Q(arrival_place__name__icontains=query)
                | Q(pov__icontains=query)
                | Q(imm_offr__email__icontains=query)
                | Q(pov__icontains=query)
                | Q(time_granted__icontains=query)
                | Q(address_in_st_lucia__icontains=query)
                | Q(tel_in_st_lucia__icontains=query)
                | Q(means_of_support__icontains=query)
                | Q(ticket_no__icontains=query)
                | Q(address_in_st_lucia__icontains=query)
            ).distinct()
        else:
            return Enquiry.objects.all()


class EnquiryDetailView(LoginRequiredMixin, DetailView):
    model = Enquiry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["remark_form"] = EnquiryRemarksCreateForm(
            initial={"enquiry": self.object}
        )
        context["subsequent_permit_form"] = SubsequentPermitCreateForm(
            initial={"enquiry": self.object}
        )
        return context


class EnquiryRemarksCreateFormView(FormView):
    form_class = EnquiryRemarksCreateForm

    def form_valid(self, form):
        enquiry_id = self.kwargs["enquiry_id"]
        comment = form.save(commit=False)
        comment.enquiry_id = enquiry_id
        comment.created_by = self.request.user
        comment.updated_by = self.request.user
        comment.save()
        messages.success(self.request, "Added")

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("enquiry-detail", args=[self.kwargs["enquiry_id"]])


class EnquireCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Enquiry
    form_class = EnquiryCreateForm
    success_message = "Enquiry created"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
