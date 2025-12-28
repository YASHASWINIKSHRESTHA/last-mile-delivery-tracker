package com.delivery.lastmile.entity;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "shipments")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Shipment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String shipmentId;

    private String customerName;

    private String otpCode;

    @Enumerated(EnumType.STRING)
    private Status status;

    private LocalDateTime deliveredAt;

    private String deliveredBy;

    public enum Status {
        PENDING,
        IN_TRANSIT,
        DELIVERED
    }
}
