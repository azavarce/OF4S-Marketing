// Toggle [data-overflow] / [data-at-end] on .scroll-hint wrappers based on
// whether their scrollable child actually overflows. Drives the right-edge
// fade and chevron so they only appear when there's somewhere to scroll to.
(function() {
  const SCROLLER_SEL = '.scroll-x, .tabs, .stepper, .data-table, .doc-stage, .stage';
  const detect = () => {
    document.querySelectorAll('.scroll-hint').forEach(hint => {
      // If the .scroll-hint element is itself a scroller, use it. Otherwise look inside.
      let scroller = null;
      if (hint.matches(SCROLLER_SEL) && hint.scrollWidth - hint.clientWidth > 4) {
        scroller = hint;
      } else {
        hint.querySelectorAll(SCROLLER_SEL).forEach(el => {
          if (el.scrollWidth - el.clientWidth > 4) scroller = el;
        });
      }
      hint.toggleAttribute('data-overflow', !!scroller);
      if (scroller && !scroller.dataset.scrollHintBound) {
        scroller.dataset.scrollHintBound = '1';
        const update = () => {
          const remaining = scroller.scrollWidth - scroller.clientWidth - scroller.scrollLeft;
          hint.toggleAttribute('data-at-end', remaining < 4);
        };
        update();
        scroller.addEventListener('scroll', update, { passive: true });
      }
    });
  };
  detect();
  window.addEventListener('resize', detect);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(detect);
})();
