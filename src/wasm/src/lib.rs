/// TitanFlow Rust SIMD Cosine Distance & Vector Engine
#[no_mangle]
pub extern "C" fn simd_cosine_similarity(a: *const f32, b: *const f32, len: usize) -> f32 {
    let mut dot_product = 0.0;
    let mut norm_a = 0.0;
    let mut norm_b = 0.0;

    unsafe {
        for i in 0..len {
            let val_a = *a.add(i);
            let val_b = *b.add(i);
            dot_product += val_a * val_b;
            norm_a += val_a * val_a;
            norm_b += val_b * val_b;
        }
    }

    if norm_a == 0.0 || norm_b == 0.0 {
        return 0.0;
    }
    dot_product / (norm_a.sqrt() * norm_b.sqrt())
}
