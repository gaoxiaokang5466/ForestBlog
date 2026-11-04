package com.liuyanzhao.ssm.blog.controller.admin;

import com.liuyanzhao.ssm.blog.entity.Page;
import com.liuyanzhao.ssm.blog.service.PageService;
import org.junit.Before;
import org.junit.Test;
import org.springframework.test.util.ReflectionTestUtils;

import java.util.Collections;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertSame;

/**
 * 后台页面编辑提交的别名校验测试。
 *
 * @author liuyanzhao
 */
public class BackPageControllerTest {

    private BackPageController controller;

    private RecordingPageService pageService;

    @Before
    public void setUp() {
        controller = new BackPageController();
        pageService = new RecordingPageService();
        ReflectionTestUtils.setField(controller, "pageService", pageService);
    }

    /**
     * 别名未被占用时应当允许保存，不能抛出空指针异常。
     */
    @Test
    public void editPageSubmitSavesWhenAliasIsUnused() {
        pageService.pageByKey = null;
        Page page = page(1, "unused-key");

        String view = controller.editPageSubmit(page);

        assertEquals("redirect:/admin/page", view);
        assertEquals(1, pageService.updateCount);
        assertSame(page, pageService.updatedPage);
        assertNotNull(page.getPageUpdateTime());
    }

    /**
     * 别名已被其他页面占用时应当拒绝保存。
     */
    @Test
    public void editPageSubmitRejectsAliasUsedByAnotherPage() {
        pageService.pageByKey = page(2, "taken-key");
        Page page = page(1, "taken-key");

        String view = controller.editPageSubmit(page);

        assertEquals("redirect:/admin/page", view);
        assertEquals(0, pageService.updateCount);
    }

    /**
     * 保留页面原有别名时应当正常保存。
     */
    @Test
    public void editPageSubmitSavesWhenAliasBelongsToSamePage() {
        pageService.pageByKey = page(1, "own-key");
        Page page = page(1, "own-key");

        String view = controller.editPageSubmit(page);

        assertEquals("redirect:/admin/page", view);
        assertEquals(1, pageService.updateCount);
        assertSame(page, pageService.updatedPage);
        assertNotNull(page.getPageUpdateTime());
    }

    private static Page page(Integer pageId, String pageKey) {
        Page page = new Page();
        page.setPageId(pageId);
        page.setPageKey(pageKey);
        page.setPageTitle("标题");
        page.setPageContent("内容");
        return page;
    }

    /**
     * 记录调用情况的 PageService 桩实现，避免测试依赖数据库。
     */
    private static class RecordingPageService implements PageService {

        private Page pageByKey;

        private int updateCount;

        private Page updatedPage;

        @Override
        public List<Page> listPage(Integer status) {
            return Collections.emptyList();
        }

        @Override
        public Page getPageByKey(Integer status, String key) {
            return pageByKey;
        }

        @Override
        public Page getPageById(Integer id) {
            return null;
        }

        @Override
        public void insertPage(Page page) {
        }

        @Override
        public void deletePage(Integer id) {
        }

        @Override
        public void updatePage(Page page) {
            updateCount++;
            updatedPage = page;
        }
    }
}
