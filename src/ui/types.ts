export interface GatewayTelemetry {
    totalRequests: number;
    cacheHits: number;
    hitRatioPercent: number;
    dollarsSaved: number;
    attacksMitigated: number;
    kernelRttMs: number;
}

export interface LatencyWaterfall {
    kernelMs: number;
    securityMs: number;
    cacheMs: number;
    inferenceMs: number;
    totalMs: number;
}
