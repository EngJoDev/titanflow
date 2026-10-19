import { GatewayTelemetry, LatencyWaterfall } from "./types";

export class TitanFlowTelemetryStream {
    private ws: WebSocket | null = null;

    connect(endpointUrl: string): void {
        this.ws = new WebSocket(endpointUrl);
        this.ws.onmessage = (event: MessageEvent) => {
            const telemetry: GatewayTelemetry = JSON.parse(event.data);
            this.renderKPIs(telemetry);
        };
    }

    private renderKPIs(t: GatewayTelemetry): void {
        console.log(`[STREAM UPDATE] Requests: ${t.totalRequests} | Hits: ${t.hitRatioPercent}%`);
    }
}
