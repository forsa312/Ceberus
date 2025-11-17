<script>
  import { onMount } from 'svelte';

  let anomalies = [];
  let loading = true;
  let error = null;

  async function fetchAnomalies() {
    try {
      const res = await fetch('http://127.0.0.1:5001/api/anomalies');
      if (!res.ok) throw new Error('Failed to fetch anomalies');
      anomalies = await res.json();
      error = null;
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    fetchAnomalies();
    const id = setInterval(fetchAnomalies, 7000);
    return () => clearInterval(id);
  });
</script>

<div class="panel">
  <div class="panel-header">
    <h2>Top Anomalies</h2>
  </div>

  {#if loading}
    <div>Scoring recent events…</div>
  {:else if error}
    <div style="color:var(--accent-red);">Error: {error}</div>
  {:else if anomalies.length === 0}
    <div>No anomalies detected in the recent window.</div>
  {:else}
    <div style="display:flex;flex-direction:column;gap:8px;">
      {#each anomalies as a, i}
        <div
          style="
            display:flex;
            flex-direction:column;
            gap:2px;
            padding:8px 10px;
            border-radius:6px;
            border:1px solid rgba(60,242,255,0.15);
          "
        >
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:13px;">
              #{i + 1} {a.device_ip || 'local'} — {a.category}/{a.event}
            </div>
            <div style="font-size:11px;color:var(--accent-blue);">
              {a.tier} · {a.severity?.toFixed ? a.severity.toFixed(1) : a.severity}
            </div>
          </div>
          <div style="font-size:11px;color:var(--text-muted);">
            {a.explanation}
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>
