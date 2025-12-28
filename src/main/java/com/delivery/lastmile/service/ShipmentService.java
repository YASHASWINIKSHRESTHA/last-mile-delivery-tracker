package com.delivery.lastmile.service;

import com.delivery.lastmile.entity.Shipment;
import com.delivery.lastmile.repository.ShipmentRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class ShipmentService {

    private final ShipmentRepository repository;

    public ShipmentService(ShipmentRepository repository) {
        this.repository = repository;
    }

    public Shipment getShipment(String shipmentId) {
        return repository.findByShipmentId(shipmentId)
                .orElseThrow(() -> new RuntimeException("Shipment not found"));
    }

    public Shipment markDelivered(String shipmentId, String otp) {
        Shipment shipment = getShipment(shipmentId);

        if (!shipment.getOtpCode().equals(otp)) {
            throw new RuntimeException("Invalid OTP");
        }

        shipment.setStatus(Shipment.Status.DELIVERED);
        shipment.setDeliveredAt(LocalDateTime.now());

        return repository.save(shipment);
    }

    // 👇 NEW METHOD (ADD THIS)
    public Shipment createShipment(String customerName) {
        Shipment shipment = new Shipment();

        shipment.setShipmentId("SHIP" + System.currentTimeMillis());
        shipment.setCustomerName(customerName);
        shipment.setOtpCode(String.valueOf((int)(Math.random() * 900000) + 100000));
        shipment.setStatus(Shipment.Status.PENDING);

        return repository.save(shipment);
    }
}
