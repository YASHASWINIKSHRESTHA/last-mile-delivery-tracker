package com.delivery.lastmile.controller;

import com.delivery.lastmile.entity.Shipment;
import com.delivery.lastmile.service.ShipmentService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/shipments")
public class ShipmentController {

    private final ShipmentService service;

    public ShipmentController(ShipmentService service) {
        this.service = service;
    }

    @GetMapping("/{shipmentId}")
    public Shipment trackShipment(@PathVariable String shipmentId) {
        return service.getShipment(shipmentId);
    }

    @PostMapping("/{shipmentId}/deliver")
    public Shipment deliverShipment(
            @PathVariable String shipmentId,
            @RequestParam String otp
    ) {
        return service.markDelivered(shipmentId, otp);
    }

    // 👇 NEW METHOD
    @PostMapping("/create")
    public Shipment createShipment(@RequestParam String customerName) {
        return service.createShipment(customerName);
    }

}
