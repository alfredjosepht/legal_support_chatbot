def is_low_confidence(confidence: float, threshold: float = 0.4) -> bool:
    return confidence < threshold
