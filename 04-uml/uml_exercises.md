# UML exercises (slide 68)

Diagrammes en Mermaid (GitHub les affiche directement).

## Exercise 1 : Hospital Management System

### Task 1 : Class diagram (basic)

```mermaid
classDiagram
    class Patient {
        -int id
        -String name
        -int age
        -String address
        +postHealthProblem()
        +payFees()
    }
    class Doctor {
        -int id
        -String name
        -String speciality
        +writePrescription()
        +receivePayment()
    }
    class Organizer {
        -int id
        -String name
        -String login
        +readProblem()
        +consultDoctor()
        +sendPrescription()
        +forwardPayment()
    }
    Patient "1..*" -- "1" Organizer : contacts
    Organizer "1" -- "1..*" Doctor : consults
```

### Task 2 : Extended class diagram

```mermaid
classDiagram
    class User {
        <<abstract>>
        -int id
        -String name
        -String password
        +login()
        +logout()
    }
    class Patient
    class Doctor
    class Organizer
    User <|-- Patient
    User <|-- Doctor
    User <|-- Organizer

    class HealthProblem {
        -String description
        -Status status
        -DateTime createdAt
    }
    class Prescription {
        -String content
        -DateTime issuedAt
    }
    class Payment {
        <<abstract>>
        -float amount
        -DateTime paidAt
        +pay()
    }
    class Cash
    class Check
    class CreditCard
    Payment <|-- Cash
    Payment <|-- Check
    Payment <|-- CreditCard

    class Status {
        <<enumeration>>
        PENDING
        IN_REVIEW
        RESOLVED
    }

    Patient "1" --> "0..*" HealthProblem : posts
    HealthProblem "1" --> "0..*" Prescription : leads to
    Doctor "1" --> "0..*" Prescription : writes
    Patient "1" --> "0..*" Payment : makes
    Prescription "1" --> "0..1" Payment : is paid by
    HealthProblem --> Status
```

Sequence diagram : le patient soumet un probleme, recoit une prescription, paie.

```mermaid
sequenceDiagram
    actor P as Patient
    participant O as Organizer
    actor D as Doctor
    P->>O: postHealthProblem()
    O->>D: consult(problem)
    D-->>O: prescription
    O-->>P: sendPrescription()
    P->>O: pay(amount)
    O->>D: forwardPayment(amount)
```

### Task 3 : Advanced

System sequence diagrams.

```mermaid
sequenceDiagram
    actor P as Patient
    participant S as System
    P->>S: register(name, age, address)
    S-->>P: accountCreated(id)
```

```mermaid
sequenceDiagram
    actor P as Patient
    participant S as System
    actor D as Doctor
    P->>S: submitProblem(description)
    S->>S: status = PENDING
    S->>D: notify(problem)
    D->>S: writePrescription(content)
    S->>S: status = RESOLVED
    S-->>P: prescription
```

```mermaid
sequenceDiagram
    actor P as Patient
    participant S as System
    participant G as PaymentStrategy
    P->>S: pay(prescriptionId, method)
    S->>G: pay(amount)
    G-->>S: confirmation
    S-->>P: receipt
```

Reponses aux questions :
- **Patient avec plusieurs medecins** : association Patient 1 -- 0..* HealthProblem, chaque probleme peut avoir plusieurs Prescription de medecins differents (Doctor 1 -- 0..* Prescription).
- **Prescription reutilisable** : la prescription garde une reference vers la precedente (previous: Prescription 0..1) et un horodatage.
- **Pattern pour les paiements** : Strategy (PaymentStrategy avec Cash, Check, CreditCard).
- **Coherence des donnees de paiement** : un Payment appartient a une seule Prescription (multiplicite 0..1) et son montant est fige a la creation.

---

## Exercise 2 : ABCD Records

### Level 1

Use case diagram.

```mermaid
flowchart LR
    M([Member]) --- PO(Place Order)
    M --- MP(Make Payment)
    C([Order Processing Clerk]) --- VM(Verify Membership)
    C --- PRO(Process Order)
    PO -. include .-> VM
    PRO -. include .-> VM
```

Class diagram.

```mermaid
classDiagram
    class Member {
        -int memberId
        -String name
        -String address
        -Date joinDate
        +placeOrder()
        +pay()
    }
    class Order {
        -int orderId
        -Date date
        -float total
        +addLine()
        +computeTotal()
    }
    class OrderProcessingClerk {
        -int clerkId
        -String name
        +verifyMembership()
        +processOrder()
    }
    Member "1" --> "0..*" Order : places
    OrderProcessingClerk "1" --> "0..*" Order : processes
```

### Level 2

Use case diagram complet.

```mermaid
flowchart LR
    subgraph System["ABCD Records system"]
        PO(Place Order)
        VM(Verify Membership)
        VA(Verify Item Availability)
        AD(Apply Discount)
        PI(Print Invoice)
        PS(Print Shipping List)
        OU(Order Unavailable Items)
        SM(Send Membership Application)
        MP(Make Payment)
        PR(Process Order)
    end
    M([Member]) --- PO
    M --- MP
    NM([Non-Member]) --- PO
    OPC([Order Processing Clerk]) --- PR
    CDC([Collection Dept Clerk]) --- MP
    PO -. include .-> VM
    PR -. include .-> VA
    PR -. include .-> PI
    PR -. include .-> PS
    AD -. extend .-> PR
    OU -. extend .-> PR
    SM -. extend .-> VM
```

Class diagram complet.

```mermaid
classDiagram
    class Member {
        -int memberId
        -String name
        -String address
    }
    class RoyalMember {
        -float discountRate
        +orderUnavailable()
    }
    Member <|-- RoyalMember
    class Item {
        <<abstract>>
        -String title
        -float price
        -boolean available
    }
    class CD
    class Tape
    Item <|-- CD
    Item <|-- Tape
    class Order {
        -int orderId
        -Date date
    }
    class OrderLine {
        -int quantity
    }
    class Invoice
    class ShippingList
    class Payment {
        <<abstract>>
        -float amount
    }
    class Cash
    class Check
    class BankDraft
    Payment <|-- Cash
    Payment <|-- Check
    Payment <|-- BankDraft
    class MembershipApplication
    class OrderProcessingClerk

    Member "1" --> "0..*" Order
    Order "1" *-- "1..*" OrderLine
    OrderLine "*" --> "1" Item
    Order "1" --> "1" Invoice
    Order "1" --> "0..1" ShippingList
    Order "1" --> "1" Payment
    OrderProcessingClerk "1" --> "0..*" Order : processes
    Member "0..1" <-- "1" MembershipApplication : creates
```

Scenario de test : un Royal member commande 2 CD (dont un indisponible) et paie par cheque.
RoyalMember -> Order avec 2 OrderLine (CD) -> l'un available = false, permis car Royal -> Payment de type Check. Le modele couvre ce cas.

### Level 3 : Sequence diagrams

Order processing flow complet.

```mermaid
sequenceDiagram
    actor M as Member
    participant C as Clerk
    participant S as System
    M->>C: placeOrder(items)
    C->>S: verifyMembership(id)
    S-->>C: valid
    C->>S: checkAvailability(items)
    S-->>C: available
    C->>S: applyDiscount()
    S-->>C: invoice, shippingList
    M->>C: pay(check)
    C->>S: recordPayment()
    S->>S: append to daily records file
```

Membership verification (succes et echec).

```mermaid
sequenceDiagram
    actor U as User
    participant S as System
    U->>S: order(memberId)
    alt member exists
        S-->>U: accepted
    else not a member
        S-->>U: send membership application form
    end
```

Payment processing (tous les types).

```mermaid
sequenceDiagram
    actor M as Member
    participant S as System
    M->>S: pay(type, amount)
    alt cash
        S->>S: recordCash(amount)
    else check
        S->>S: recordCheck(number, amount)
    else bank draft
        S->>S: recordDraft(reference, amount)
    end
    S-->>M: receipt
```

Item reordering pour les Royal members.

```mermaid
sequenceDiagram
    actor R as RoyalMember
    participant S as System
    R->>S: order(unavailableItem)
    S->>S: check isRoyal
    S->>S: createBackorder(item)
    S-->>R: backorder confirmed, priority
```
