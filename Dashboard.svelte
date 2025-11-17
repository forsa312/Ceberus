<script>
  import { onMount } from 'svelte';

  let loading = true;
  let error = null;
  let data = {
    anomalies_24h: 0,
    devices: 0,
    events_24h: 0,
    threat_level: 'LOW'
  };

  async function fetchDashboard() {
    try {
      const res = await fetch('http://127.0.0.1:5001/api/dashboard');
      if (!res.ok) throw new Error('Failed to fetch dashboard');
      data = await res.json();
      error = null;
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    fetchDashboard();
    const id = setInterval(fetchDashboard, 5000);
    return () => clearInterval(id);
  });
</script>

<div class="panel">
  <div class="panel-header">
    <h2>Network Posture</h2>
    <div class="pulse-dot"></div>
  </div>

  {#if loading}
    <div>Loading telemetry…</div>
  {:else if error}
    <div style="color: var(--accent-red);">Error: {error}</div>
  {:else}
    <div style="display:flex;gap:16px;flex-wrap:wrap;">
      <div>
        <div style="font-size:11px;color:var(--text-muted);">Threat Level</div>
        <div style="font-size:20px;color:var(--accent-blue);">{data.threat_level}</div>
      </div>
      <div>
        <div style="font-size:11px;color:var(--text-muted);">Anomalies (24h)</div>
        <div style="font-size:18px;">{data.anomalies_24h}</div>
      </div>
      <div>
        <div style="font-size:11px;color:var(--text-muted);">Active Devices</div>
        <div style="font-size:18px;">{data.devices}</div>
      </div>
      <div>
        <div style="font-size:11px;color:var(--text-muted);">Events (24h)</div>
        <div style="font-size:18px;">{data.events_24h}</div>
      </div>
    </div>
  {/if}
</div>
