from rest_framework import serializers

class DepositSerializers(serializers.Serializer):
    deposit_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class WithdrawalSerializers(serializers.Serializer):
    withdrawal_amount= serializers.DecimalField(max_digits=10, decimal_places=2)

class TransferSerializers(serializers.Serializer):
    transfer_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    destination_account= serializers.DecimalField(max_digits=6, decimal_places=0)