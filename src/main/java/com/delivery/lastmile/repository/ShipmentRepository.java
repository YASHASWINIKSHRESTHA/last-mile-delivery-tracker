package com.delivery.lastmile.repository;

import com.delivery.lastmile.entity.Shipment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ShipmentRepository extends JpaRepository<Shipment, Long> {

    Optional<Shipment> findByShipmentId(String shipmentId);
}
